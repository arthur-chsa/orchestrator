import os, glob, shutil

from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def _exec(**context):
    print("Testing change of service account")
    
default_args = {
    'start_date' : datetime(2021,1,1)
}

with DAG(
    'Exec',
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    schedule_interval=None
) as dag:

    exec = PythonOperator(
        task_id = 'exec',
        python_callable=_exec
    )