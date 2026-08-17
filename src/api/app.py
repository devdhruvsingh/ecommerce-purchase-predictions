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


@app.route("/")
def home():
    return "E-Commerce Purchase Prediction API is running"

@app.route("/predict", methods=["POST"])
def predicts():
    data = request.get_json()
    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return jsonify({
        "prediction" : bool(prediction),
        "purchase_probability" : float(probability)
                })

if __name__ == "__main__":
    app.run(debug=True)