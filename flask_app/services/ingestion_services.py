import json
import os

DATA_PATH = "data/lake/bronze"
os.makedirs(DATA_PATH, exist_ok=True)

def save_event(data):
    event = {
        "user": data["user"],
        "movie": data["movie"],
        "genre": data["genre"],
        "platform": data["platform"],
        "rating": data["rating"],
        "review": data["review"],
        "timestamp": data["timestamp"]
    }

    file_path = os.path.join(DATA_PATH, "events.json")

    with open(file_path, "a") as f:
        f.write(json.dumps(event) + "\n")

    return {"status": "success"}



