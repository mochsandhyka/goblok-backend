from app import app
from flask import Flask, jsonify
import os


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=False, port=os.getenv("PORT", default=5000))
