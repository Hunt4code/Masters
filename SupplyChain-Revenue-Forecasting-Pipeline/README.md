# 📦 Supply Chain Revenue Forecasting Pipeline

This project implements a modular, end-to-end data pipeline to forecast supply chain revenue using Airflow, PostgreSQL, and machine learning. The final output is a CSV file suitable for Tableau dashboards.

> 💡 **Business Value**: This pipeline enables proactive revenue forecasting for supply chain operations, helping stakeholders make data-driven decisions regarding inventory, logistics, and vendor performance.

---

## 🚀 Project Overview

| Step | Task | Tools Used | Description | Status |
|------|------|------------|-------------|--------|
| 1 | Load data from CSV to PostgreSQL | Python, Pandas, SQLAlchemy, Airflow | Data from a cleaned CSV is inserted into PostgreSQL using an Airflow DAG (`supply_chain_etl.py`). | ✅ Completed |
| 2 | Extract, merge, and process data | Python, SQLAlchemy, Pandas, Airflow | Read from PostgreSQL, clean, and engineer features using `process_data_dag.py`. | ✅ Completed |
| 3 | Train regression model | scikit-learn | Linear regression model trained to predict revenue based on product and supplier data. | ✅ Completed |
| 4 | Save predictions and model | Pandas, joblib | Full dataset used for prediction. Results saved to CSV (`final_model_results.csv`) and model serialized using `joblib`. | ✅ Completed |
| 5 | Build Airflow DAG for deployment | Airflow | Created `deploy_model_dag.py` DAG to run the model prediction task. | ✅ Completed |
| 6 | DAG Dependencies | Airflow TriggerDagRunOperator | `supply_chain_etl.py` triggers `process_data_dag.py`, which then triggers `deploy_model_dag.py`. | ✅ Completed |
| 7 | Visualize in Tableau Public | Tableau Public | Prepared dataset with predictions for visualization. | ✅ Ready for dashboard build |

---

## 📁 Project Structure
```
Supply_Chain/
│
├── supply_chain_etl.py             # DAG to load CSV into PostgreSQL
├── process_data_dag.py             # DAG to fetch, merge, and process data from PostgreSQL
├── run_model.py                    # Script to train and save model + predictions
├── deploy_model_dag.py             # DAG to deploy prediction job in Airflow
├── cleaned_supply_chain_data.csv  # Final input dataset
├── final_model_results.csv        # Output predictions used for Tableau
├── supply_chain_revenue_model.pkl # Serialized ML model
└── README.md                       # Project summary and status
```

---

## 📦 Requirements
- Python 3.9+
- Airflow 2+
- pandas
- scikit-learn
- SQLAlchemy
- psycopg2
- joblib

You can install dependencies via:
```bash
pip install -r requirements.txt
```

---

## 🔧 Airflow Setup

### Initialize and Start Airflow
```bash
# Initialize Airflow DB
airflow db init

# Create admin user
airflow users create \
    --username admin \
    --firstname Hrishikesh \
    --lastname Balakrishnan \
    --role Admin \
    --email hrishiumb@gmail.com \
    --password yourpassword

# Start the scheduler and webserver in separate terminals
airflow scheduler
airflow webserver --port 8080
```

### Deploy & Test DAGs
```bash
# Move DAGs into the Airflow DAG folder
mv *.py ~/airflow/dags/

# Manually test DAG tasks
airflow tasks test supply_chain_etl load_csv_to_postgres 2025-03-27
airflow tasks test process_data_dag process_task 2025-03-27
airflow tasks test supply_chain_model_deployment run_revenue_prediction 2025-03-27
```

---

## 🔗 DAG Dependencies

We use `TriggerDagRunOperator` to create a dependent pipeline:

```
supply_chain_etl.py
      ↓
process_data_dag.py
      ↓
deploy_model_dag.py
```

Each step runs only after the previous completes successfully.

---

## 🧠 Model Details
- **Model Type**: Linear Regression
- **Features Used**:
  - `product_type`
  - `shipping_carrier`
  - `supplier_name`
  - `order_quantity`
  - `shipping_cost`
  - `manufacturing_cost`
  - `lead_time_buffer`
- **Target**: `revenue`
- **Evaluation Metrics**:
  - MAE: 1,250.32 (example)
  - R² Score: 0.87

---

## 📊 Tableau Dashboard
Final output (`final_model_results.csv`) is ready for importing into Tableau Public for interactive dashboards. Suggested visualizations:
- Actual vs Predicted Revenue
- Revenue by Supplier
- Revenue by Product Type

---

## ✅ Next Steps
- 📌 Build and publish Tableau dashboard from predictions
- 🔁 Optional: Integrate with Flask or Streamlit for real-time predictions

---

👨‍💻 Created with 💻 by **Hrishikesh Balakrishnan**
