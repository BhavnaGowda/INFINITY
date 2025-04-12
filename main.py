from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.optimizer import optimize_resources
import joblib
import numpy as np

# Load models (ensure filenames match what's saved in save_models.py)
stay_model = joblib.load("models/stay_model.pkl")
cost_model = joblib.load("models/xgb_model.pkl")  # Corrected filename
admissions_model = joblib.load("models/arima_model.pkl")

app = FastAPI()

# Request model schema
class PatientData(BaseModel):
    age: float
    dm: int
    htn: int
    cad: int
    ckd: int
    season_num: int = 0
    stay: float = 0.0  # Optional for cost prediction

@app.get("/")
def root():
    return {"msg": "Hospital Resource Management API"}

@app.post("/predict-stay")
def get_stay_prediction(data: PatientData):
    try:
        features = np.array([[data.age, data.dm, data.htn, data.cad, data.ckd]])
        print("DEBUG: stay features shape ->", features.shape)
        print("DEBUG: stay model expects ->", stay_model.n_features_in_)
        assert features.shape[1] == stay_model.n_features_in_
        prediction = stay_model.predict(features)[0]
        return {"predicted_stay": float(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Stay prediction error: {str(e)}")

@app.post("/predict-cost")
def get_cost_prediction(data: PatientData):
    try:
        # Correct feature order and count based on model training
        features = np.array([[data.season_num, data.stay, data.age, data.dm, data.htn, data.cad, data.ckd]])
        print("DEBUG: cost features shape ->", features.shape)
        print("DEBUG: cost model expects ->", cost_model.n_features_in_)
        assert features.shape[1] == cost_model.n_features_in_
        prediction = cost_model.predict(features)[0]
        return {"predicted_cost": float(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cost prediction error: {str(e)}")

@app.get("/forecast-admissions")
def forecast_admissions():
    try:
        print("DEBUG: Forecasting next 30 days of admissions...")
        forecast_result = admissions_model.get_forecast(steps=30)
        forecast = forecast_result.predicted_mean
        print("DEBUG: Forecast shape ->", forecast.shape)
        print("DEBUG: Forecast preview ->", forecast.head().to_list())
        return {"forecast": forecast.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Admissions forecast error: {str(e)}")

@app.get("/optimize-resources")
def get_optimization():
    try:
        result = optimize_resources()
        return {"optimization_result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Optimization error: {str(e)}")
