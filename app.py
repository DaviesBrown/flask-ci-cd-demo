from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask CI/CD pipeline!"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/api/info")
def info():
    return jsonify({
        "app_name": "Flask CI/CD Demo",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat(),
        "endpoints": ["/", "/health", "/api/info"]
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
