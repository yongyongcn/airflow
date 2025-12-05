FROM apache/airflow:3.1.3
USER root
COPY requirements.txt /
# RUN pip install --no-cache-dir apache-airflow-providers-mysql
RUN /home/airflow/.local/bin/python -m pip install --no-cache-dir -r /requirements.txt

USER airflow