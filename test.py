import secrets
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Generate and store API keys
def generate_api_key(user_name):
    api_key = secrets.token_hex(32)  # Generate a 64-character key
    conn = sqlite3.connect("api_keys.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO api_keys (user_name, api_key, created_at) VALUES (?, ?, ?)",
        (user_name, api_key, datetime.now()),
    )
    conn.commit()
    conn.close()
    return api_key

@app.route("/generate_key", methods=["POST"])
def generate_key():
    data = request.json
    if not data or "user_name" not in data:
        return jsonify({"error": "user_name is required"}), 400

    user_name = data["user_name"]
    api_key = generate_api_key(user_name)
    return jsonify({"user_name": user_name, "api_key": api_key})

if __name__ == "__main__":
    app.run(debug=True)
