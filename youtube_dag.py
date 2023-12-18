from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import googleapi

default_args = {
    'owner' : 'airflow',
    'depends_on_past' : False,
    'start_date' : datetime(2023,12,16),
    'email' : ['airflow@example.com'],
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 1,
    'retry_delay' : timedelta(minutes=1)    
}

dag = DAG(
    'youtube_dag',
    default_args = default_args,
    decsription = 'My first etl code'
)

run_etl = PythonOperator(
    task_id ='complete_youtube_etl',
    python_callable = googleapi.youtubeETL,
    dag=dag
)

run_etl