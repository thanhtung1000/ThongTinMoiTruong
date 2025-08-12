from flask import Flask, request, jsonify
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cho phép truy cập từ trình duyệt

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/data", methods=["POST"])
def post_data():
    data = request.json
    data["Time"] = datetime.utcnow().isoformat()
    db.collection("environment").add(data)
    return jsonify({"status": "success"}), 200

@app.route("/data", methods=["GET"])
def get_data():
    station = request.args.get("station")
    from_time = request.args.get("from")
    to_time = request.args.get("to")

    from_dt = datetime.fromisoformat(from_time)
    to_dt = datetime.fromisoformat(to_time)

    docs = db.collection("environment").stream()
    result = []
    for doc in docs:
        d = doc.to_dict()
        t = datetime.fromisoformat(d["Time"]).replace(tzinfo=None)
        if from_dt <= t <= to_dt:
            if station.lower() == "all" or d["Name"].lower() == station.lower():
                result.append(d)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
