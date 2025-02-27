#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('final_xgb_model_threshold_0.4.pkl')

st.title("Thyroid Cancer Risk Prediction")

st.write("Enter the patient details to predict the risk of thyroid cancer.")

# User Input Fields
family_history = st.radio("Family History of Thyroid Cancer?", ('Yes', 'No'))
gender = st.radio("Gender", ('Male', 'Female'))
iodine_deficiency = st.radio("Iodine Deficiency?", ('Yes', 'No'))
radiation_exposure = st.radio("Radiation Exposure?", ('Yes', 'No'))
obesity = st.radio("Obesity?", ('Yes', 'No'))
smoking = st.radio("Smoking?", ('Yes', 'No'))
diabetes = st.radio("Diabetes?", ('Yes', 'No'))
age = st.slider("Age", 1, 100, 30)  # Default age = 30

# Convert user input to numerical format
def preprocess_input(family_history, gender, iodine_deficiency, radiation_exposure, obesity, smoking, diabetes, age):
    return np.array([[
        1 if family_history == 'Yes' else 0,
        1 if gender == 'Male' else 0,
        1 if iodine_deficiency == 'Yes' else 0,
        1 if radiation_exposure == 'Yes' else 0,
        1 if obesity == 'Yes' else 0,
        1 if smoking == 'Yes' else 0,
        1 if diabetes == 'Yes' else 0,
        age
    ]])

# Predict function
def predict_thyroid_risk(patient_data):
    prob_malignant = model.predict_proba(patient_data)[:, 1]
    threshold = 0.3  # Adjusted for better recall
    prediction = (prob_malignant > threshold).astype(int)
    return "Malignant" if prediction[0] == 1 else "Benign"

# Button to make predictions
if st.button("Predict"):
    patient_data = preprocess_input(family_history, gender, iodine_deficiency, radiation_exposure, obesity, smoking, diabetes, age)
    result = predict_thyroid_risk(patient_data)
    st.subheader(f"Prediction: {result}")


# In[ ]:




