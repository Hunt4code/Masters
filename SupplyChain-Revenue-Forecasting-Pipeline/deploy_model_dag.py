#!/usr/bin/env python
# coding: utf-8

# In[1]:


# dags/deploy_model_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append('/Users/apple/Desktop/Git/Supply_Chain/run_model.py')  # update path as needed
from run_model import run_prediction

default_args = {
    'owner': 'airflow',
    'start_date': datetime.today(),
    'retries': 1
}

with DAG(
    dag_id='supply_chain_model_deployment',
    default_args=default_args,
    schedule_interval='@weekly',  # change as needed
    catchup=False
) as dag:
    
    deploy_model = PythonOperator(
        task_id='run_revenue_prediction',
        python_callable=run_prediction
    )


# In[ ]:




