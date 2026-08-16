from .load import load_raw_data


def validate_data(df):
    """Run basic validation checks on the raw dataset."""

    print("=" * 50)
    print("DATASET VALIDATION")
    print("=" * 50)

    print(f"\nShape: {df.shape}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nUnique Values:")
    print(df.nunique())

    print("\nTarget Distribution:")
    print(df["Revenue"].value_counts())

    print("\nTarget Distribution (%):")
    print(df["Revenue"].value_counts(normalize=True) * 100)


if __name__ == "__main__":
    data = load_raw_data()
    validate_data(data)
