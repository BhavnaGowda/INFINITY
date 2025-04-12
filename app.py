import streamlit as st
import requests

st.title("🏥 Predictive Hospital Resource Management")

st.header("🔹 Predict Patient Stay Duration")
with st.form("stay_form"):
    age = st.number_input("Age", min_value=0, value=60)
    dm = st.selectbox("Diabetes (DM)", [0, 1])
    htn = st.selectbox("Hypertension (HTN)", [0, 1])
    cad = st.selectbox("Coronary Artery Disease (CAD)", [0, 1])
    ckd = st.selectbox("Chronic Kidney Disease (CKD)", [0, 1])
    season_num = st.selectbox("Season (1=Winter, 2=Spring, 3=Summer, 4=Fall)", [1, 2, 3, 4])
    submitted = st.form_submit_button("Predict Stay")

    if submitted:
        data = {
            "age": age,
            "dm": dm,
            "htn": htn,
            "cad": cad,
            "ckd": ckd,
            "season_num": season_num
        }
        response = requests.post("https://infinity-api-backend.onrender.com/predicted_stay", json=data)
        if response.status_code == 200:
            st.success(f"📅 Predicted Length of Stay: {response.json()['predicted_stay']} days")
        else:
            st.error("❌ Prediction failed.")
st.header("🔹 Predict Treatment Cost")
with st.form("cost_form"):
    stay = st.number_input("Length of Stay (in days)", min_value=0.0, value=4.0)
    age = st.number_input("Age", min_value=0, value=60)
    dm = st.selectbox("Diabetes (DM)", [0, 1])
    htn = st.selectbox("Hypertension (HTN)", [0, 1])
    cad = st.selectbox("Coronary Artery Disease (CAD)", [0, 1])
    ckd = st.selectbox("Chronic Kidney Disease (CKD)", [0, 1])
    season_num = st.selectbox("Season (1=Winter, 2=Spring, 3=Summer, 4=Fall)", [1, 2, 3, 4])
    submitted = st.form_submit_button("Predict Cost")

    if submitted:
        data = {
            "age": age,
            "dm": dm,
            "htn": htn,
            "cad": cad,
            "ckd": ckd,
            "season_num": season_num,
            "stay": stay
        }
        response = requests.post("https://infinity-api-backend.onrender.com/predict-cost", json=data)
        if response.status_code == 200:
            st.success(f"💰 Predicted Treatment Cost: ${response.json()['predicted_cost']}")
        else:
            st.error("❌ Prediction failed.")
st.header("🔹 Forecast Admissions for the Next 30 Days")
with st.form("forecast_form"):
    submitted = st.form_submit_button("Get Admissions Forecast")

    if submitted:
        response = requests.get("https://infinity-api-backend.onrender.com/forecast-admissions")
        if response.status_code == 200:
            forecast = response.json()["forecast"]
            st.line_chart(forecast)  # Display forecast as a line chart
        else:
            st.error("❌ Forecast failed.")
st.header("🔹 Optimize Resources (Beds & Staff)")
with st.form("optimization_form"):
    submitted = st.form_submit_button("Optimize Resources")

    if submitted:
        response = requests.get("https://infinity-api-backend.onrender.com/optimize-resources")
        if response.status_code == 200:
            result = response.json()["optimization_result"]
            st.write(f"Optimized Resource Allocation: Beds: {result[0]}, Staff: {result[1]}")
        else:
            st.error("❌ Optimization failed.")
