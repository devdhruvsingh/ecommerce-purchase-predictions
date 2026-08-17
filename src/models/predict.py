from pathlib import Path

import joblib


MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "models"
    / "purchase_prediction_pipeline.pkl"
)


def load_model():
    """Load the trained purchase prediction pipeline."""
    return joblib.load(MODEL_PATH)


def predict_purchase(data):
    """Predict purchase outcome and probability."""
    model = load_model()

    prediction = model.predict(data)
    probability = model.predict_proba(data)[:, 1]

    return prediction, probability
