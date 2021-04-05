import mlflow

with mlflow.start_run():
    mlflow.log_param("p", 0)
    mlflow.log_metric("m", 1)
    mlflow.set_tag("t", "a")
    print("tracking uri", mlflow.get_tracking_uri())


import psycopg2 as pg
import pandas as pd
import pandas.io.sql as psql
import os

connection = pg.connect(os.environ.get("MLFLOW_TRACKING_URI"))
#my_table   = pd.read_sql_table('table_name', connection)

LIST_TABLE = """
SELECT table_name
FROM information_schema.tables WHERE
table_schema = 'public'
ORDER BY table_name
"""

TABLE_SCHEMA = """
SELECT *
FROM information_schema.columns
WHERE table_name = '{}';
"""

print(pd.read_sql(LIST_TABLE, connection))
df = pd.read_sql(TABLE_SCHEMA.format("metrics"), connection)

for idx, row in df.iterrows():
    print("=" * 80)
    print(idx, row)
# another_attempt= psql.read_sql("SELECT * FROM my-table-name", connection)
