# backend-flask/main.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


#Django API URL 
DJANGO_API_URL = "http://127.0.0.1:8000/api/products/"


@app.route("/")
def home():
    return "Flask API connected to Django! Go to /items to see products."


# Get all products from Django
@app.route("/items", methods=["GET"])
def get_items():
    try:
        response = requests.get(DJANGO_API_URL)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)