FROM python:3.10-slim

WORKDIR /app

COPY flask_app/ /app/

RUN pip install flask boto3 minio

EXPOSE 5003

CMD ["python", "app.py"]






