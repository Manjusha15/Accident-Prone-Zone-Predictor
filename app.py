import streamlit as st
import pandas as pd
import joblib

# Load saved model
model = joblib.load("accident_prediction_model.pkl")

st.title("🚦 Accident Prone Zone Predictor")

st.write("Enter road and traffic conditions to predict accident risk.")

# User Inputs
weather = st.selectbox("Select Weather", ["Clear", "Rainy", "Foggy"])
road = st.selectbox("Select Road Condition", ["Dry", "Wet", "Snow"])
traffic = st.selectbox("Select Traffic Density", ["Low", "Medium", "High"])
speed = st.slider("Select Speed", 30, 120)
time = st.selectbox("Select Time of Day", ["Morning", "Afternoon", "Night"])

if st.button("Predict"):
    
    # Manual encoding (same logic as training)
    weather_map = {"Clear": 0, "Foggy": 1, "Rainy": 2}
    road_map = {"Dry": 0, "Snow": 1, "Wet": 2}
    traffic_map = {"High": 0, "Low": 1, "Medium": 2}
    time_map = {"Afternoon": 0, "Morning": 1, "Night": 2}

    input_data = pd.DataFrame({
        "Weather": [weather_map[weather]],
        "Road_Condition": [road_map[road]],
        "Traffic_Density": [traffic_map[traffic]],
        "Speed": [speed],
        "Time_of_Day": [time_map[time]]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Accident Prone Zone – Avoid Travel")
    else:
        st.success("✅ Safe to Travel")
