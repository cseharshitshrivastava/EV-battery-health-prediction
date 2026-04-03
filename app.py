import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🔋 Battery Health Prediction System")

st.write("Enter battery parameters:")

voltage = st.number_input("Voltage (V)", value=3.7)
current = st.number_input("Current (A)", value=1.5)
temperature = st.number_input("Temperature (°C)", value=25.0)
cycle = st.number_input("Charge Cycles", value=100)

if st.button("Predict Battery Health"):
    input_data = np.array([[voltage, current, temperature, cycle]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Battery Capacity: {round(prediction[0], 2)}")
