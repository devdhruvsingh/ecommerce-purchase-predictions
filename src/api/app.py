from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from pathlib import Path


app = Flask(__name__)

# Allow the frontend to communicate with the API
CORS(app)


# Find the project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]


# Load the trained ML pipeline
MODEL_PATH = PROJECT_ROOT / "models" / "purchase_prediction_pipeline.pkl"

model = joblib.load(MODEL_PATH)


# Required features
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
    "ProductTimeRatio"
]


# Features that must be between 0 and 1
RATE_FEATURES = [
    "BounceRates",
    "ExitRates",
    "SpecialDay"
]


# Valid categorical values
VALID_MONTHS = [
    "Feb",
    "Mar",
    "May",
    "June",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
]


VALID_VISITOR_TYPES = [
    "Returning_Visitor",
    "New_Visitor",
    "Other"
]


# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "E-Commerce Purchase Prediction API is running!"
    })


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    # Get JSON data
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "error": "Invalid JSON data"
        }), 400

    if not data:
        return jsonify({
            "error": "No JSON data provided"
        }), 400


    # Check missing features
    missing_features = [
        feature
        for feature in REQUIRED_FEATURES
        if feature not in data
    ]

    if missing_features:
        return jsonify({
            "error": "Missing required information",
            "missing_features": missing_features
        }), 400


    # Check numeric features
    numeric_features = [
        feature
        for feature in REQUIRED_FEATURES
        if feature not in ["Month", "VisitorType", "Weekend"]
    ]

    for feature in numeric_features:

        if not isinstance(data[feature], (int, float)):
            return jsonify({
                "error": "Invalid data type",
                "feature": feature,
                "expected": "number"
            }), 400


        # Check negative values
        if data[feature] < 0:
            return jsonify({
                "error": "Negative values are not allowed",
                "feature": feature
            }), 400


    # Check rate features
    for feature in RATE_FEATURES:

        if data[feature] < 0 or data[feature] > 1:
            return jsonify({
                "error": "Invalid rate value",
                "feature": feature,
                "expected": "value between 0 and 1"
            }), 400


    # Check Month
    if data["Month"] not in VALID_MONTHS:
        return jsonify({
            "error": "Invalid month",
            "valid_months": VALID_MONTHS
        }), 400


    # Check VisitorType
    if data["VisitorType"] not in VALID_VISITOR_TYPES:
        return jsonify({
            "error": "Invalid visitor type",
            "valid_visitor_types": VALID_VISITOR_TYPES
        }), 400


    # Check Weekend
    if not isinstance(data["Weekend"], bool):
        return jsonify({
            "error": "Invalid Weekend value",
            "expected": "true or false"
        }), 400


    # Create dataframe
    input_data = pd.DataFrame([data])


    try:

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Get purchase probability
        probability = model.predict_proba(input_data)[0][1]


        return jsonify({
            "prediction": bool(prediction),
            "purchase_probability": float(probability)
        })


    except Exception as error:

        return jsonify({
            "error": "Prediction failed",
            "details": str(error)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)