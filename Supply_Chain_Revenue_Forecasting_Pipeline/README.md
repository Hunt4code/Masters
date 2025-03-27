# 📦 Supply Chain Revenue Forecasting Pipeline

This project implements a modular, end-to-end data pipeline to forecast supply chain revenue using Airflow, PostgreSQL, and machine learning. The final output is a CSV file suitable for Tableau dashboards.


---

## 🚀 Project Overview

| Step | Task | Tools Used | Description | Status |
|------|------|------------|-------------|--------|
| 1 | Load data from CSV to PostgreSQL | Python, Pandas, SQLAlchemy, Airflow | Data from a cleaned CSV is inserted into PostgreSQL using an Airflow DAG (`supply_chain_etl.py`). | ✅ Completed |
| 2 | Extract and merge data from PostgreSQL | Python, SQLAlchemy, Pandas | Data from four normalized tables (`products`, `orders`, `suppliers`, `quality_checks`) is read and merged. | ✅ Completed |
| 3 | Clean and engineer features | Python, Pandas | Feature engineering: unit revenue, unit cost, lead time buffer. | ✅ Completed |
| 4 | Train regression model | scikit-learn | Linear regression model trained to predict revenue based on product and supplier data. | ✅ Completed |
| 5 | Save predictions and model | Pandas, joblib | Predicted revenue added to the full dataset and saved as CSV. Model serialized using `joblib`. | ✅ Completed |
| 6 | Build Airflow DAG for deployment | Airflow | Created `deploy_model_dag.py` DAG to run the model prediction task. | ✅ Completed |
| 7 | Deploy and test model using Airflow | Airflow CLI | Deployed model via Airflow task, verified with `airflow tasks test`. | ✅ Completed |
| 8 | Visualize in Tableau Public | Tableau Public | Prepared `final_model_results.csv` with predictions for visualization. | ✅ Ready for dashboard build |

---

## 📁 Project Structure
```
Supply_Chain/
│
├── supply_chain_etl.py             # DAG to load CSV into PostgreSQL
├── run_model.py                    # Script to train and save model + predictions
├── deploy_model_dag.py             # DAG to deploy prediction job in Airflow
├── cleaned_supply_chain_data.csv   # Final input dataset
├── final_model_results.csv         # Output predictions used for Tableau
├── supply_chain_revenue_model.pkl  # Serialized ML model
├── airflow.cfg / webserver_config.py # Airflow config files (if customized)
└── README.md                        # Project summary and status
```

---

## ⚙️ Airflow Setup & Commands

### Initializing and Running Airflow:
```bash
# Initialize Airflow database
airflow db init

# Create a user (if needed)
airflow users create \
    --username admin \
    --firstname Hrishikesh \
    --lastname Balakrishnan \
    --role Admin \
    --email hrishiumb@gmail.com \
    --password yourpassword

# Start the scheduler (in a new terminal tab)
airflow scheduler

# Start the webserver (in a new terminal tab)
airflow webserver --port 8080
```

### DAG Deployment & Task Execution:
```bash
# Move your DAG file to the Airflow DAGs folder
mv deploy_model_dag.py ~/airflow/dags/

# Ensure your model script is also present
mv run_model.py ~/airflow/dags/

# Run the DAG task manually for a specific date
airflow tasks test supply_chain_model_deployment run_revenue_prediction 2025-03-27
```

---

## 🧠 Model Details
- **Type**: Linear Regression
- **Features**: `product_type`, `shipping_carrier`, `supplier_name`, `order_quantity`, `shipping_cost`, `manufacturing_cost`, `lead_time_buffer`
- **Target**: `revenue`
- **Evaluation Metrics**: MAE, R² Score

---

## ✅ Next Steps
- Build and publish Tableau dashboard from `final_model_results.csv`
- Optionally: Integrate with Flask or Streamlit for dynamic prediction interface

---

## 👤 Author
**Hrishikesh Balakrishnan**  
📧 hrishiumb@gmail.com  
🔧 Tools: Python, Airflow, PostgreSQL, Pandas, scikit-learn, Tableau Public

