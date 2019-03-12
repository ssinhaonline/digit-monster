from flask import request, abort, jsonify
from app import app

@app.route("/digit-monster/v1.0/predict", methods=["POST"])
def do_predict():
    return jsonify({"status": "OK"}), 201