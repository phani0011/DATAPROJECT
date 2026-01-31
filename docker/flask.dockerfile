FROM python:3.9

WORKDIR /app

COPY flask_app /app
RUN pip install flask

CMD ["python", "app.py"]

