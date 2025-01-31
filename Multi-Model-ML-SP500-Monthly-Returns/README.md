# 📈 Multi-Model Machine Learning for Predicting Monthly Returns of S&P 500 Stocks

## 📌 Project Overview
Predicting stock returns is a challenging task due to the dynamic nature of financial markets. This project applies **machine learning techniques** to predict **monthly returns of S&P 500 stocks** using **historical stock prices and financial indicators**. The approach leverages **Random Forest, Decision Trees, Ridge Regression, and Neural Networks** to explore different predictive models.

## 🔍 Key Features
- **Multi-Model Approach**: Evaluates multiple machine learning models (Linear Regression with Ridge, Decision Tree, Random Forest, and MLP Regressor).
- **Comprehensive Data Processing**: Extracts **daily stock prices, financial ratios, and market trends** to build robust features.
- **Feature Engineering**: Computes **Sharpe ratio, volatility measures, skewness, and cumulative returns** to enhance predictions.
- **Machine Learning Pipelines**: Implements **hyperparameter tuning, cross-validation, and feature scaling** to optimize performance.
- **Data Sources**: Scrapes **Yahoo Finance, Wikipedia, and SEC Edgar** for stock prices and financial indicators.

## 📂 Folder Structure
Multi_Model_ML_SP500_Monthly_Returns/
│── README.md            # Project documentation
│── data/                # Processed datasets with stock features
│── notebooks/           # Jupyter Notebooks for feature engineering & model training
│── models/              # Trained machine learning models
│── final_report.pdf     # Detailed project findings and analysis
│── presentation.pptx    # Summary of project results

## 🛠 Tech Stack
- **Languages**: Python
- **Libraries**: Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, XGBoost, TensorFlow
- **Data Sources**: Yahoo Finance API, SEC Edgar, Wikipedia
- **Modeling Techniques**: Random Forest, Decision Trees, Ridge Regression, Neural Networks

## 📊 Dataset Details
- **Timeframe**: 2010 - 2023
- **Data Points**: 1.6M+ records
- **Features Extracted**:
  - Average Daily Returns Over a Month
  - Standard Deviation of Returns (Volatility)
  - Sharpe Ratio (Risk-Adjusted Return)
  - Skewness of Returns
  - Cumulative Returns Over 3, 6, 9, and 12 months
  - End-of-Month Closing Price
  - Trading Volume Trends
  - Financial Ratios from Edgar (ROE, P/E, Debt-to-Equity)

## 🏆 Model Performance
| Model           | Train R² | Test R² | Train MSE | Test MSE |
|----------------|---------|---------|-----------|-----------|
| **Ridge Regression**  | 0.0164  | 0.0089  | 0.0071  | 0.0072  |
| **Decision Tree**  | 0.0391  | 0.0126  | 0.0069  | 0.0071  |
| **Random Forest** | 0.7681  | 0.0373  | 0.0016  | 0.0070  |
| **Neural Network (MLP Regressor)** | 0.0379  | 0.0186  | 0.0070  | 0.0070  |

✅ **Random Forest outperformed other models**, capturing market trends with **higher accuracy and lower error**.

## 🚀 How to Run the Project
### **1️⃣ Install Dependencies**
pip install -r requirements.txt

### **2️⃣ Run Data Preprocessing**
python scripts/preprocess_data.py

### **3️⃣ Train the Model**
python scripts/train_model.py --model random_forest

### **4️⃣ Evaluate Performance**
python scripts/evaluate_model.py

## 📈 Key Findings
- **Random Forest provides the best predictive accuracy** for stock returns.
- **Feature engineering improves prediction by capturing stock volatility and market trends**.
- **Hyperparameter tuning and cross-validation enhance model robustness**.
- **Financial indicators from Edgar improve model interpretability**.

## 🛑 Limitations
- **Stock market fluctuations introduce high variance, limiting generalization**.
- **Deep learning models require more computational power to outperform tree-based models**.
- **More feature selection and data sources (news sentiment, macroeconomic indicators) could improve performance**.

## 🔮 Future Enhancements
- **Deep Learning Integration**: Implement **LSTMs and transformers** for time-series forecasting.
- **Alternative Data Sources**: Add **news sentiment analysis and social media trends**.
- **Live Market Predictions**: Deploy a **real-time prediction model**.

## 📜 References
- **Yahoo Finance API**: [Link](https://www.yahoofinanceapi.com/)
- **SEC Edgar Filings**: [Link](https://www.sec.gov/edgar.shtml)
- **Wikipedia S&P 500 List**: [Link](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
- **Stock Price Prediction with Machine Learning** [[IEEE](https://ieeexplore.ieee.org/document/8990165)]
- **Random Forest in Financial Forecasting** [[MDPI](https://www.mdpi.com/2227-7390/9/15/1746)]

## 📬 Contact
For questions or collaboration, reach out to:
- **Author**: Hrishikesh Balakrishnan
- **GitHub**: [Hunt4code](https://github.com/Hunt4code)
- **Email**: hrishiumb@gmail.com


