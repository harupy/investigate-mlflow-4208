FROM python:3.7

# RUN pip install mlflow==1.15.0 psycopg2

# Install mlflow containing a patch for the issue
RUN pip install git+https://github.com/dolfinus/mlflow.git@fix_1.15_migration psycopg2

COPY mlflow_log.py /mlflow_log.py
