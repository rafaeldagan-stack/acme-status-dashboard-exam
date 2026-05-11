import os
import socket
from flask import Flask, jsonify, redirect, request, abort, render_template

app = Flask(__name__)

PORT = int(os.getenv("PORT", 5000))
VERSION = os.getenv("VERSION", "1.0.0")
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY environment variable is required")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/status")
def api_status_redirect():
    return redirect("/api/v1/status", code=302)


@app.route("/api/v1/status")
def api_status():
    return jsonify({
        "status": "ok",
        "hostname": socket.gethostname(),
        "version": VERSION
    })


@app.route("/api/v1/secret")
def secret():
    header_key = request.headers.get("X-API-Key")

    if header_key != API_KEY:
        abort(401)

    return jsonify({
        "message": "you found the secret"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
