import os
from flask import Flask, jsonify

app = Flask(__name__)

VERSION = os.getenv("VERSION", "undefined")

@app.route("/health")
def health():
    return "OK", 200

@app.route("/version")
def version():
    return jsonify({"version": VERSION})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
