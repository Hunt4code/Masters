#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# dags/process_data_dag.py
from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
import os


# PostgreSQL connection setup
DB_URI = "postgresql://username:password@localhost:5432/supply_chain"
engine = create_engine(DB_URI)

# Define your merge and clean logic here
def process_and_clean_data():
    def fetch_table(name):
        return pd.read_sql(f"SELECT * FROM {name}", con=engine)

    products = fetch_table("products")
    orders = fetch_table("orders")
    suppliers = fetch_table("suppliers")
    quality = fetch_table("quality_checks")

    # Merge
    df = products.merge(orders, on="sku", how="left")
    df = df.merge(suppliers, on="supplier_name", how="left")
    df = df.merge(quality, on=["sku", "supplier_id"], how="left")

    # Clean and feature engineer
    df['revenue_per_unit'] = df['revenue'] / (df['number_sold'] + 1e-5)
    df['cost_per_unit'] = df['order_cost'] / (df['order_quantity'] + 1e-5)
    df['lead_time_buffer'] = df['manufacturing_lead_time'] - df['supplier_lead_time']
    df.dropna(subset=['revenue', 'order_quantity'], inplace=True)

    df.to_csv("cleaned_supply_chain_data.csv", index=False)
    print("Saved cleaned data to cleaned_supply_chain_data.csv")

# DAG definition
default_args = {
    'owner': 'airflow',
    'retries': 1
}

dag = DAG(
    'supply_chain_data_processing',
    default_args=default_args,
    start_date=datetime(2025, 3, 27),
    schedule_interval=None,
    catchup=False
)

process_data_task = PythonOperator(
    task_id='process_and_clean_data',
    python_callable=process_and_clean_data,
    dag=dag
)

# DAG dependencies 
trigger_model_dag = TriggerDagRunOperator(
    task_id='trigger_deploy_model_dag',
    trigger_dag_id='supply_chain_model_deployment',
    wait_for_completion=True
)

process_task >> trigger_model_dag

