from fastapi import FastAPI
from pydantic import BaseModel

import joblib
import pandas as pd

from pathlib import Path


# ------------------
# Load trained model
# ------------------

MODEL_PATH = Path("models/trained/random_forest_model.pkl")

model = joblib.load(MODEL_PATH)

# ------------------
# Create FastAPI app
# ------------------
app = FastAPI()

# ------------------------
# Define request structure
# ------------------------

class HouseFeatures(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int


# ------------------
# Health check route
# ------------------

@app.get("/")
def home():

    return {
        "message" : "House Price Prediction API Running"
    }

# ----------------
# Prediction route
# ----------------
@app.post("/predict")
def predict(data: HouseFeatures):

    input_data = pd.DataFrame([{
        "area": data.area,
        "bedrooms": data.bedrooms,
        "bathrooms": data.bathrooms,
        "stories": data.stories,
        "parking": data.parking
    }])

    prediction = model.predict(input_data)[0]

    return {
        "predicted_house_price": round(
            float(prediction),
            2
        )
    }
    
