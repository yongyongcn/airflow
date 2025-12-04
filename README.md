# Prerquisite
- install uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv init airflow-project
cd airflow-project
mkdir -p ./dags ./logs ./plugins ./config
uv venv
source .venv/bin/activate

```
- download docker-compose.ymal
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
```
- set the uer id
```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
- init the database
```bash
docker compose up airflow-init
```

# Usage
- start airflow
```bash
source .venv/bin/activate
docker compose up -d
```
login with: airflow@airflow

- go to browser
localhost:8080


- stop airflow
```bash
docker compse down
```