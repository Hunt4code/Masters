#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def load_data():
    # Connection setup
    connection_url = URL.create(
        drivername="postgresql+psycopg2",
        username="postgres",
        password="postgres",
        host="localhost",
        port=5432,
        database="postgres"
    )
    engine = create_engine(connection_url, echo=True)

    # Read and clean data
    df = pd.read_csv("/Users/apple/Desktop/Git/Supply_Chain/supply_chain_data.csv")
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    products_df = df[['sku', 'product_type', 'price', 'availability', 'stock_levels']].drop_duplicates().copy()
    products_df.rename(columns={'stock_levels': 'stock_level'}, inplace=True)

    suppliers_df = df[['supplier_name', 'location', 'lead_time', 'production_volumes',
                       'manufacturing_lead_time', 'manufacturing_costs']].drop_duplicates().copy()
    suppliers_df.rename(columns={'lead_time': 'supplier_lead_time'}, inplace=True)

    orders_df = df[['sku', 'order_quantities', 'shipping_times',
                    'shipping_carriers', 'shipping_costs']].drop_duplicates().copy()
    orders_df.rename(columns={'shipping_costs': 'shipping_cost'}, inplace=True)

    quality_df = df[['sku', 'supplier_name', 'inspection_results', 'defect_rates']].drop_duplicates().copy()
    quality_df.rename(columns={
        'inspection_results': 'inspection_result',
        'defect_rates': 'defect_rate'
    }, inplace=True)

    # Use engine.connect() with isolation level
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as connection:
        products_df.to_sql('products', con=connection, if_exists='append', index=False)
        suppliers_df.to_sql('suppliers', con=connection, if_exists='append', index=False)
        orders_df.to_sql('orders', con=connection, if_exists='append', index=False)
        quality_df.to_sql('quality_checks', con=connection, if_exists='append', index=False)

# DAG definition
default_args = {
    'owner': 'airflow',
    'start_date': datetime.today(),
    'retries': 1,
}

with DAG(
    dag_id='supply_chain_etl',
    default_args=default_args,
    schedule_interval='@once',
    catchup=False
) as dag:

    run_etl = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=load_data
    )


# DAG dependencies
trigger_process_dag = TriggerDagRunOperator(
    task_id='trigger_process_data_dag',
    trigger_dag_id='process_data_dag',
    wait_for_completion=True
)

load_csv_to_postgres >> trigger_process_dag

