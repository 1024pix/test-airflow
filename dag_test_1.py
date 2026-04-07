import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

from assets import ASSET_TEST_1_FIRST_TASK

with DAG(
    dag_id="test_1",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
):
    first_task = EmptyOperator(task_id="first_task", outlets=ASSET_TEST_1_FIRST_TASK)
    second_task = EmptyOperator(task_id="second_task")
    first_task >> second_task
