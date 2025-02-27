# 🏥 ThyroPredict 

Thyroid Cancer Risk Prediction - AI-Powered Diagnostic Tool

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)](https://www.tensorflow.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.5%2B-green)](https://xgboost.readthedocs.io/)

**An AI-powered machine learning model to predict the risk of thyroid cancer based on patient health data.**

An AI-powered machine learning model to predict the risk of thyroid cancer based on patient health data. This project applies Deep Learning (Neural Networks), XGBoost, Bayesian Optimization, and SHAP Explainability to classify patients as Benign (0) or Malignant (1) based on risk factors like family history, radiation exposure, obesity, and more.

🚀 **Designed for real-world deployment with a Flask API and a Streamlit Web App.**

---

🔥 Key Features

- Advanced ML & Deep Learning: XGBoost, Neural Networks, and Ensemble Models.
- Class Imbalance Handling: Implements scale_pos_weight and class_weight techniques.
- Optimized Hyperparameters: Utilizes Bayesian Optimization & Differential Evolution Strategy (DES).
- Explainability with SHAP: Understand and interpret model predictions.
- Interactive Web Interface: Deployed using Streamlit for user-friendly interactions.
- Production-Ready API: RESTful Flask API for integration with other systems.

---

## 📌 Project Structure
```
Thyroid-Cancer-Prediction
│── README.md              # Project Documentation
│── requirements.txt        # Required Python packages
│── ThyroPredict_app.py                  # Streamlit Web App
│── ThyroPredict_Flask_app.py            # Flask API
│── ThyroPredict.ipynb     # Jupyter Notebook for Model Development
│── final_xgb_model_threshold_0.4.pkl  # Saved XGBoost Model
│── fnn_trained_model.h5      # Saved Neural Network Model
│── data                     # Dataset & Preprocessing Scripts
│── notebooks                # Exploratory Data Analysis & Model Training
```

---

## 📌 Dataset
**Source**: [Thyroid Cancer Risk Dataset](https://www.kaggle.com/datasets/bhargavchirumamilla/thyroid-cancer-risk-dataset)  
- **Features Used**:
  - `Age`, `Family_History`, `Radiation_Exposure`, `Iodine_Deficiency`
  - `Obesity`, `Smoking`, `Diabetes`, `TSH_Level`, `T3_Level`, `T4_Level`, `Nodule_Size`
  - **Target Variable:** `Diagnosis` (Benign = 0, Malignant = 1)

---

## 📌 Installation & Setup
### 🔹 Step 1: Clone the Repository
```
git clone https://github.com/Hunt4code/Thyroid-Cancer-Prediction.git
cd Thyroid-Cancer-Prediction
```

### 🔹 Step 2: Create Virtual Environment & Install Dependencies
```
python -m venv venv
source venv/bin/activate  # (On Windows use `venv\Scripts\activate`)
pip install -r requirements.txt
```

---

## 📌 Usage
### 🔹 Run the Streamlit Web App
```
streamlit run ThyroPredict_app.py
```
This opens an **interactive web interface** where users can input patient details and get predictions.

### 🔹 Run the Flask API
```
python ThyroPredict_Flask_app.py
```
This starts a **REST API** where you can send patient data and receive risk predictions.

**Test the API using Python:**
```python
import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "family_history": 1,  
    "gender": 0,  
    "iodine_deficiency": 1,
    "radiation_exposure": 0,
    "obesity": 1,
    "smoking": 1,
    "diabetes": 0,
    "age": 50
}

response = requests.post(url, json=data)
print(response.json())  # Output: {'prediction': 'Benign' or 'Malignant'}
```

---

## 📌 Model Explainability (SHAP)
The **SHAP (Shapley Additive Explanations)** technique helps interpret predictions:
```python
import shap

explainer = shap.Explainer(best_xgb_balanced)
shap_values = explainer(X_test_selected)
shap.summary_plot(shap_values, X_test_selected)
```
👉 **Provides feature importance insights to help doctors understand predictions.**

---

## 📌 Future Improvements
- **Feature Engineering Enhancements**: Introduce polynomial features and feature interactions  
- **Better Hyperparameter Optimization**: Use Optuna or AutoML for automated tuning  
- **Deploy to Cloud**: Deploy Streamlit on **Streamlit Cloud** & API on **AWS/GCP/Azure**  
- **Ensemble Models**: Combine Neural Networks, XGBoost, and Logistic Regression for improved accuracy  

---

## 📌 Author & Contributions
**👤 Hrishikesh Balakrishnan**  
🔗 **GitHub**: [Hunt4code](https://github.com/Hunt4code)  
🔗 **LinkedIn**: [Hrishikesh Balakrishnan](https://www.linkedin.com/in/hrishikesh-balakrishnan/)  

**Contributions Welcome!** 🎉  
Feel free to fork this repo, make improvements, and submit pull requests.

