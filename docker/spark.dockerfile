FROM apache/spark:3.5.1

WORKDIR /app
COPY spark_jobs /app

CMD ["/opt/spark/bin/spark-submit", "process_data.py"]



