import json
import sqlite3
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello, World! 123"

@app.route("/time", methods=["GET"])
def main():
    date = datetime.now()
    return str(date)


