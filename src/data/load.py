from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "online_shoppers_intention.csv"


def load_raw_data() -> pd.DataFrame:
    """Load the raw UCI Online Shoppers dataset."""
    return pd.read_csv(RAW_DATA_PATH)


if __name__ == "__main__":
    df = load_raw_data()

    print(f"Dataset shape: {df.shape}")
    print("\nColumns:")
    print(df.columns.tolist())
