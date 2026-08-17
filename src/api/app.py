from flask import Flask, request, jsonify 
import joblib
import pandas as pd
from pathlib import Path


app = Flask(__name__)

# find the project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# loading the trained ml pipeline
MODEL_PATH = PROJECT_ROOT / "models" / "purchase_prediction_pipeline.pkl"

model = joblib.load(MODEL_PATH)

REQUIRED_FEATURES = [
    "Administrative",
    "Administrative_Duration",
    "Informational",
    "Informational_Duration",
    "ProductRelated",
    "ProductRelated_Duration",
    "BounceRates",
    "ExitRates",
    "PageValues",
    "SpecialDay",
    "Month",
    "OperatingSystems",
    "Browser",
    "Region",
    "TrafficType",
    "VisitorType",
    "Weekend",
    "TotalPages",
    "TotalDuration",
    "AvgTimePerPage",
    "ProductEngagementRatio",
    "ProductTimeRatio"]


@app.route("/predict", methods = ["POST"])
def predict():
    # getting the json data
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No JSON data provided"

        }), 400

    # for missing features
    missing_features = [
        feature for feature in REQUIRED_FEATURES
        if feature not in data
    ]
    if missing_features:
        return jsonify({
            "error" : "Missing required information",
            "missing_features": missing_features
        }), 400

    input_data = pd.DataFrame([data])

    try :
        # making the prediction
        prediction = model.predict(input_data)[0]

        probability = model.predict_prob(input_data)[0][1]

        return jsonify({
            "prediction": bool(prediction),
            "purchase prediction": float(probability)
        })

    except Exception as error:
        return jsonify({
            "error": "Prediction failed",
            "details": str(error)
        }), 400

if __name__ == "__main__":
    app.run(debug=True)