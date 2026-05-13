import pandas as pd
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = ROOT_PATH / "data" / "raw" / "housing.csv"
PROCESSED_DATA_PATH = ROOT_PATH / "data" / "processed" / "processed_housing.csv"

def process_data(): 
    df = pd.read_csv(RAW_DATA_PATH)

    df = df.dropna()

    # save processed data
    PROCESSED_DATA_PATH.parent.mkdir(exist_ok= True, parents=True)

    df.to_csv(PROCESSED_DATA_PATH, index= False)

    print("Data processing completed!")
    print(df.head())

if __name__ == "__main__":
    process_data()