# flask_app/services/ingestion_services.py

import json
from minio import Minio
from io import BytesIO
from datetime import datetime

client = Minio(
    "minio:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

BUCKET = "lake"
BRONZE_PATH = "bronze/events.json"


def save_event(data):
    try:
        # Add timestamp
        data["timestamp"] = str(datetime.now())

        # Get existing file (if exists)
        try:
            obj = client.get_object(BUCKET, BRONZE_PATH)
            existing = obj.read().decode()
            events = existing.strip().split("\n")
        except:
            events = []

        events.append(json.dumps(data))

        final_data = "\n".join(events)

        client.put_object(
            BUCKET,
            BRONZE_PATH,
            BytesIO(final_data.encode()),
            length=len(final_data),
            content_type="application/json"
        )

        return {"status": "success", "written_to": BRONZE_PATH}

    except Exception as e:
        return {"status": "error", "message": str(e)}









