import pandas as pd
from pathlib import Path


ROOT_PATH = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT_PATH / "data" / "processed" / "processed_housing.csv"
OUTPUT_PATH = ROOT_PATH / "data" / "processed" / "featured_housing.csv"

def engineer_features():
    df = pd.read_csv(INPUT_PATH)

    # example features
    if "total_rooms" in df.columns and "households" in df.columns:
        df["room_per_household"] = ( df["total_rooms"] / df["households"] )

    df.to_csv(OUTPUT_PATH, index= False)

    print("feature engineering completed.")
    print(df.head())

if __name__ == "__main__":
    engineer_features()