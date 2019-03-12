from flask import request, abort, jsonify
from app import app
from predict import predict
import numpy as np

@app.route("/digit-monster/v1.0/predict", methods=["POST"])
def do_predict():
    request_payload = request.json

    # Check for payload validity
    if not request_payload or "X" not in request_payload:
        abort(400)
    try:
        # Build successful response
        successful_response = dict(
            status="OK",
            predicted_labels= predict(X=request_payload["X"])
        )

        # If suggested labels are provided, check for size mismatch
        # and then calculate truth of labels
        if "suggested_labels" in request_payload:
            if len(request_payload["suggested_labels"]) != len(request_payload["X"]):
                successful_response["message"] = "WARN: Prediction success, " \
                                "possible mismatch in size of X and suggested_labels"
            successful_response["is_correct"] = (np.array(request_payload["suggested_labels"]) \
                                == np.array(successful_response["predicted_labels"])).tolist()

        # If no suggested labels are provided, respond with successful
        # response as is
        return jsonify(successful_response), 201

    except Exception as e:
        # If there's a failure during prediction, respond with
        # appropriate failure message
        return jsonify(dict(
            status="Failed",
            message="ERROR: Prediction failed, error trace: [{}]".format(e.message)
        ))