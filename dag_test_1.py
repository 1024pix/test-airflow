import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator

from assets import ASSET_TEST_1_FIRST_TASK


with DAG(
    dag_id="test_1",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
):
    first_task = BashOperator(task_id="first_task", bash_command="echo task_1", outlets=ASSET_TEST_1_FIRST_TASK)
    second_task = BashOperator(task_id="second_task", bash_command="echo task_2")
    third_task = EmptyOperator(task_id="third_task")

    first_task >> second_task >> third_task
