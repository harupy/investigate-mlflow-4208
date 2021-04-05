import os

import pymysql
import pandas as pd
import sqlalchemy  as sa

import mlflow

with mlflow.start_run():
    mlflow.log_param("p", 0)
    mlflow.log_metric("m", 1)
    mlflow.set_tag("t", "a")
    print("tracking uri", mlflow.get_tracking_uri())


connection = sa.create_engine(os.environ.get("MLFLOW_TRACKING_URI"))

TABLE_SCHEMA = """
SELECT *
FROM information_schema.columns
WHERE table_name = '{}';
"""

df = pd.read_sql(TABLE_SCHEMA.format("metrics"), connection)

print(df[["COLUMN_NAME", "COLUMN_DEFAULT"]])
