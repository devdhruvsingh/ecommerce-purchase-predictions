from pathlib import Path

import joblib


MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "models"
    / "purchase_prediction_pipeline.pkl"
)


def load_trained_model():
    """Load the trained purchase prediction pipeline."""
    return joblib.load(MODEL_PATH)


if __name__ == "__main__":
    model = load_trained_model()
    print("Trained model loaded successfully.")
    print(model)
