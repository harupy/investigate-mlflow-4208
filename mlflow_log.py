import mlflow

with mlflow.start_run():
    mlflow.log_param("p", 0)
    mlflow.log_metric("m", 1)
    mlflow.set_tag("t", "a")
    print("tracking uri", mlflow.get_tracking_uri())
