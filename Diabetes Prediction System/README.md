# GlycoCheck - Diabetes Prediction System

## 📌 Project Overview

GlycoCheck is a **machine learning-based system** designed to predict diabetes risk using **demographic, lifestyle, medical history, and lab test results**. This project includes **data analysis, model training, evaluation, and deployment** via a **Flask API and Streamlit UI**.

## 📂 Dataset

- **Records:** 5,292
- **Features:** 27 (Numerical & Categorical)
- **Target Variable:** `Diabetes_Status` (Yes/No)

### **Feature Breakdown**

- **Numerical Features:** Age, BMI, Cholesterol Level, Fasting Blood Sugar, HBA1C, Glucose Tolerance Test, C-Protein Level, etc.
- **Categorical Features:** Gender, Family History, Diet Type, Smoking Status, Alcohol Intake, Hypertension, etc.

## 🔍 Exploratory Data Analysis (EDA)

Key insights from data analysis:

- **Age:** Most individuals are between 30–60 years old.
- **BMI:** Majority fall in the overweight category (Mean = 27.46).
- **HBA1C & Fasting Blood Sugar:** Strong indicators of diabetes risk.
- **Outliers Detected:** Cholesterol, Blood Sugar, C-Protein levels show extreme values.

## 🏆 Machine Learning Models

I trained three models to predict diabetes risk:

| Model                   | Accuracy (%) |
| ----------------------- | ------------ |
| **Logistic Regression** | 82.4         |
| **Random Forest**       | 87.2         |
| **XGBoost**             | **89.5**     |

✅ **Best Model:** XGBoost (89.5% accuracy) 🚀

### **Feature Importance (Top 5)**

1. **HBA1C** (Most Important)
2. **Fasting Blood Sugar**
3. **Glucose Tolerance Test**
4. **BMI**
5. **Cholesterol Level**

## 🚀 Deployment

### **Flask API**

- **Runs a REST API for real-time diabetes prediction**
- **Accepts JSON inputs and returns predictions**

**Run API:**

```bash
python app.py
```

**Test API with cURL:**

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [45, 1, 32.5, 1, 2, 1, 0, 0, 2, 1, 190, 100, 140, 6.5, 80, 0.95, 1, 0, 1, 0, 2, 0, 120, 30, 7, 0, 1]}'
```

✅ **Expected Output:**

```json
{"prediction": "Diabetic"}
```

### **Streamlit Web App**

- **User-friendly interface for diabetes prediction**
- **Accepts manual inputs & returns predictions instantly**

**Run Streamlit App:**

```bash
streamlit run app.py
```

## 🔮 Future Enhancements

- **Hyperparameter tuning for better accuracy**
- **Deploy API on AWS/GCP for cloud access**
- **Feature explainability with SHAP/LIME**

## 📜 Conclusion

I successfully developed GlycoCheck, a **data-driven AI solution** for **diabetes risk assessment**. The project demonstrates **data analysis, machine learning, and deployment skills**, making it a practical tool for real-world healthcare applications. 🚀

---

### 🔗 Connect with Me

Feel free to reach out for discussions or improvements! 📧 Email: [[your.email@example.com](mailto\:your.email@example.com)]\
🔗 LinkedIn: [Your LinkedIn Profile]\
🐍 GitHub: [Your GitHub Profile]

