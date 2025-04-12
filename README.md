# 🏥 Predictive Hospital Resource Management

## 🎯 Project Goal
Design an AI system that forecasts patient admissions, stay duration, and resource costs to optimize staffing, bed allocation, and equipment usage.

---

## ✅ Phase 1: Data Preparation & Model Training

- Cleaned the dataset (handled missing values, formatted dates)
- Derived features like SEASON_NUM from Admission Date
- Built and trained:
  - Stay Prediction Model: DecisionTreeRegressor
  - Cost Prediction Model: XGBoost
  - Admission Forecast Model: ARIMA
- Saved all models to /models folder using joblib

📦 Deliverables:
- models/stay_model.pkl
- models/xgb_model.pkl
- models/arima_model.pkl

---

## ✅ Phase 2: Backend API (FastAPI)

- Created main.py for FastAPI server
- Defined Pydantic BaseModel for patient input schema
- Implemented endpoints:
  - /predict-stay → returns predicted stay duration
  - /predict-cost → returns estimated resource cost
  - /forecast-admissions → returns 30-day ARIMA forecast
  - /optimize-resources → returns optimal beds & staff allocation
- Added debug logs and error handling
- Tested endpoints using Swagger UI (/docs)

📦 Deliverable:
- FastAPI backend that serves ML predictions

---

## ✅ Phase 3: Frontend Interface

- Built a lightweight web frontend (React or Streamlit)
- Input forms for patient data
- Displayed predictions for:
  - Stay Duration
  - Resource Cost
  - 30-Day Admissions Forecast (Graph)
- Integrated frontend with backend via API calls

📦 Deliverable:
- User-friendly interface for hospital administrators

---

## ✅ Phase 4: Deployment & Extras

- Dockerized the app (optional for portability)
- Deployed backend (Render / Railway / EC2 / Localhost)
- Added features:
  - Authentication (login for admins)
  - Alerting System (e.g., if predicted stay > 10 days)
  - Dashboard with charts (Plotly, Chart.js)
  - Downloadable reports (CSV / PDF)
- Prepared slides and live demo for hackathon presentation

📦 Deliverables:
- Live or locally deployed full-stack app
- Demo-ready system with fully integrated UI and backend

---
