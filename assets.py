from airflow.sdk import Asset

ASSET_TEST_1_FIRST_TASK = Asset("table://pg/asset")
