from __future__ import annotations
import sys
import os
import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import airflow.providers.mysql as mysql_providers
 #.operators.mysql import MySqlOperator
import airflow.providers.postgres
#.operators.postgres import PostgresOperator

from common import add

# Define default arguments for the DAG
with DAG(
    dag_id="simple_hello_dag",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["example", "tutorial"],
    doc_md="""
    # Simple Hello World DAG
    A basic example DAG that runs two sequential tasks.
    """,
) as dag:
    
    task_0 = PythonOperator(
        task_id="what_is_5_plus_7",
        python_callable=add,
        op_args=[5, 7],
    )

    # Task 1: Print a welcome message
    task_1 = BashOperator(
        task_id="print_start_message",
        bash_command="echo 'Starting the Hello World workflow...'",
    )

    # Task 2: Print the execution date
    task_2 = BashOperator(
        task_id="print_execution_date",
        bash_command="echo 'YY says today: The execution date is {{ ds }}'",
    )

    # Define the task dependency: task_1 must run before task_2
    task_1 >> task_2 >> task_0