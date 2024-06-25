import os, glob, shutil

from datetime import datetime
from utilities.api import *
from utilities.pipeline import *
from utilities.general import *

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def _exec(**context):
    #shutil.rmtree('/usr/local/airflow/temp')
    execution_date = datetime.combine(datetime.fromtimestamp(context['ti'].execution_date.timestamp()).date(), datetime.min.time())
    #execution_date = datetime.combine(datetime.fromtimestamp(context['ti'].execution_date.timestamp()).date(), datetime.min.time())
    #execution_date_yesterday = execution_date - timedelta(days=1)
    #print(execution_date)
    #print(execution_date_yesterday)
    
    print(getCalculatedDate(execution_date, 'previous_month_start'))
    print(getCalculatedDate(execution_date, 'previous_month_end'))
    print(getCalculatedDate(execution_date, 'current_month_start'))
    print(getCalculatedDate(execution_date, 'current_month_end'))
    print(getCalculatedDate(execution_date, 'next_month_start'))
    print(getCalculatedDate(execution_date, 'next_month_end'))

    print(getCalculatedDate(execution_date, 'previous_month_start_ts'))
    print(getCalculatedDate(execution_date, 'previous_month_end_ts'))
    print(getCalculatedDate(execution_date, 'current_month_start_ts'))
    print(getCalculatedDate(execution_date, 'current_month_end_ts'))
    print(getCalculatedDate(execution_date, 'next_month_start_ts'))
    print(getCalculatedDate(execution_date, 'next_month_end_ts'))

    print(getCalculatedDate(execution_date, 'previous_week_start'))
    print(getCalculatedDate(execution_date, 'previous_week_end'))
    print(getCalculatedDate(execution_date, 'previous_week_start_ts'))
    print(getCalculatedDate(execution_date, 'previous_week_end_ts'))
    
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