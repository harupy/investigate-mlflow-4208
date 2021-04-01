investigate https://github.com/mlflow/mlflow/issues/4208

```
git clone https://github.com/harupy/investigate-mlflow-4208.git
docker-compose --file docker-compose-mysql.yml up --build
docker-compose --file docker-compose-postgres.yml up --build
docker-compose --file docker-compose-sqlite.yml up --build
```
