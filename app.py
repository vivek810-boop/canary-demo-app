from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def home():
    return jsonify({
        "application": "canary-demo",
        "message": "Welcome to Canary Demo Application",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname()
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": APP_VERSION
    }), 200


@app.route("/version")
def version():
    return jsonify({
        "application": "canary-demo",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname()
    })


@app.route("/products")
def products():
    return jsonify({
        "version": APP_VERSION,
        "products": [
            {
                "id": 101,
                "name": "Laptop",
                "price": 75000
            },
            {
                "id": 102,
                "name": "Keyboard",
                "price": 2500
            },
            {
                "id": 103,
                "name": "Mouse",
                "price": 1200
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)