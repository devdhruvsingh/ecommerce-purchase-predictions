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
    "ProductTimeRatio"
]


NUMERIC_NON_NEGATIVE = [
    "Administrative",
    "Administrative_Duration",
    "Informational",
    "Informational_Duration",
    "ProductRelated",
    "ProductRelated_Duration",
    "PageValues",
    "OperatingSystems",
    "Browser",
    "Region",
    "TrafficType",
    "TotalPages",
    "TotalDuration",
    "AvgTimePerPage",
    "ProductEngagementRatio",
    "ProductTimeRatio"
]


RATE_FEATURES = [
    "BounceRates",
    "ExitRates",
    "SpecialDay"
]


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


@app.route("/")
def home():
    return "E-Commerce Purchase Prediction API is running!"


@app.route("/predict", methods=["POST"])
def predict():

    # getting the json data
    try :
        data = request.get_json()
    except Exception:
        return jsonify({
            "error": "Invalid JSON data"
        }), 400

    if not data:
        return jsonify({
            "error": "No JSON data provided"
        }), 400


    # checking for missing features
    missing_features = [
        feature for feature in REQUIRED_FEATURES
        if feature not in data
    ]

    if missing_features:
        return jsonify({
            "error": "Missing required information",
            "missing_features": missing_features
        }), 400


    # checking numeric values
    for feature in NUMERIC_NON_NEGATIVE:

        if not isinstance(data[feature], (int, float)):
            return jsonify({
                "error": f"{feature} must be a number"
            }), 400

        if data[feature] < 0:
            return jsonify({
                "error": f"{feature} cannot be negative"
            }), 400


    # checking rate values
    for feature in RATE_FEATURES:

        if not isinstance(data[feature], (int, float)):
            return jsonify({
                "error": f"{feature} must be a number"
            }), 400

        if not 0 <= data[feature] <= 1:
            return jsonify({
                "error": f"{feature} must be between 0 and 1"
            }), 400


    # checking month
    if data["Month"] not in VALID_MONTHS:
        return jsonify({
            "error": "Invalid Month",
            "allowed_values": VALID_MONTHS
        }), 400


    # checking visitor type
    if data["VisitorType"] not in VALID_VISITOR_TYPES:
        return jsonify({
            "error": "Invalid VisitorType",
            "allowed_values": VALID_VISITOR_TYPES
        }), 400


    # checking weekend
    if not isinstance(data["Weekend"], bool):
        return jsonify({
            "error": "Weekend must be true or false"
        }), 400


    # converting the data into dataframe
    input_data = pd.DataFrame([data])


    try:

        # making the prediction
        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]

        return jsonify({
            "prediction": bool(prediction),
            "purchase_probability": float(probability)
        })


    except Exception as error:

        return jsonify({
            "error": "Prediction failed",
            "details": str(error)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)