import mlflow

with mlflow.start_run():
    mlflow.log_param("a", 0)
    mlflow.log_metric("b", 0)

    print("tracking uri", mlflow.get_tracking_uri())
