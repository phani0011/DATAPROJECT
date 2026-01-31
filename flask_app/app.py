from flask import Flask, request, render_template
from services.ingestion_services import save_event
from datetime import datetime
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = {
            "user": request.form.get("name"),
            "movie": request.form.get("movie"),
            "genre": request.form.get("genre"),
            "platform": request.form.get("platform"),
            "rating": int(request.form.get("rating", 0)),
            "review": request.form.get("review"),
            "timestamp": str(datetime.now())
        }

        save_event(data)
        return render_template("thankyou.html")

    except Exception as e:
        return f"Error occurred: {str(e)}"

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)

