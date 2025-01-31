#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import joblib
import numpy as np

# Load trained model and scaler
rf_model = joblib.load("random_forest_optimized.pkl")
scaler = joblib.load("scaler.pkl")

# Define feature names (from dataset)
feature_names = [
    "Age", "Gender", "BMI", "Family_History", "Physical_Activity", "Diet_Type",
    "Smoking_Status", "Alcohol_Intake", "Stress_Level", "Hypertension", "Cholesterol_Level",
    "Fasting_Blood_Sugar", "Postprandial_Blood_Sugar", "HBA1C", "Heart_Rate",
    "Waist_Hip_Ratio", "Urban_Rural", "Health_Insurance", "Regular_Checkups",
    "Medication_For_Chronic_Conditions", "Pregnancies", "Polycystic_Ovary_Syndrome",
    "Glucose_Tolerance_Test_Result", "Vitamin_D_Level", "C_Protein_Level", "Thyroid_Condition"
]

# Streamlit UI
st.title("Diabetes Prediction App")
st.write("Enter patient details to predict the likelihood of diabetes.")

# Create input fields
input_data = []
for feature in feature_names:
    value = st.number_input(f"{feature}", min_value=0.0, max_value=300.0, value=0.0)
    input_data.append(value)

# Predict button
if st.button("Predict"):
    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)  # Scale input features
    prediction = rf_model.predict(input_scaled)[0]
    
    st.write("### Prediction:")
    st.write("✅ **Diabetic**" if prediction == 1 else "❌ **Non-Diabetic**")

