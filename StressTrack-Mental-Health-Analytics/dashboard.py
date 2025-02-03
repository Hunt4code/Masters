#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
st.title("📊 Depression Prediction Dashboard")
st.sidebar.header("🔍 Select Analysis")

# Load cleaned dataset
df = pd.read_csv("Student Depression Dataset.csv")

# Feature Selection
features = [
    "Academic Pressure", "Financial Stress", "Work/Study Hours",
    "Job Satisfaction", "Family History of Mental Illness",
    "Dietary Habits", "Have you ever had suicidal thoughts ?"
]

df_ml = df[features + ["Depression"]]
df_ml = pd.get_dummies(df_ml, drop_first=True)

# Train-Test Split
X = df_ml.drop(columns=["Depression"])
y = df_ml["Depression"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost Model
xgb_model = XGBClassifier(n_estimators=200, max_depth=5, learning_rate=0.1, random_state=42)
xgb_model.fit(X_train, y_train)

# Predictions
y_pred_xgb = xgb_model.predict(X_test)

# Model Performance
accuracy = accuracy_score(y_test, y_pred_xgb)
report = classification_report(y_test, y_pred_xgb, output_dict=True)

# Sidebar Options
option = st.sidebar.radio("Select Analysis", ["Model Performance", "Feature Importance", "Make Predictions"])

# 📌 **1. Model Performance Visualization**
if option == "Model Performance":
    st.subheader("📊 Model Accuracy & Metrics")

    # Accuracy Display
    st.metric("XGBoost Accuracy", f"{accuracy:.4f}")

    # Classification Report Table
    st.write("### Classification Report")
    st.dataframe(pd.DataFrame(report).T)

# 📌 **2. Feature Importance Visualization**
elif option == "Feature Importance":
    st.subheader("🔍 Feature Importance")

    # Get feature importances
    feature_importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": xgb_model.feature_importances_
    }).sort_values(by="Importance", ascending=False)

    # Plot Feature Importance
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Importance", y="Feature", data=feature_importance, palette="Blues_r")
    plt.title("Feature Importance in Depression Prediction")
    st.pyplot(plt)

# 📌 **3. Make Predictions on New Data**
elif option == "Make Predictions":
    st.subheader("📝 Enter Data for Depression Prediction")

    # User Input Form
    input_data = {}
    for feature in X.columns:
        input_data[feature] = st.slider(feature, float(df_ml[feature].min()), float(df_ml[feature].max()), float(df_ml[feature].median()))

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Prediction
    prediction = xgb_model.predict(input_df)[0]
    prediction_text = "Likely Depressed" if prediction == 1 else "Not Depressed"
    st.subheader(f"🔮 Prediction: **{prediction_text}**")

