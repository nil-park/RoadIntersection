import json
from os.path import dirname, abspath, join as ospj
from flask import Flask, send_file, send_from_directory
from controller import getStatus
app = Flask(__name__)

ROOT = abspath(dirname(dirname(__file__)))

@app.route("/", methods=["GET"])
def index():
    return send_file(ospj(ROOT, "ui", "index.html"))

@app.route("/favicon.ico", methods=["GET"])
def favicon():
    return send_file(ospj(ROOT, "ui", "favicon.ico"))

@app.route("/images/<path:path>", methods=["GET"])
def images(path):
    return send_from_directory(ospj(ROOT, "ui", "images"), path)

@app.route("/api/status", methods=["GET"])
def status():
    return json.dumps(getStatus()), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
