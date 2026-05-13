from dotenv import load_dotenv

import os

load_dotenv()

MLFLOW_TRACKING_URI = os.getenv(
    "MLFLOW_TRACKING_URI")

MODEL_PATH = os.getenv(
    "MODEL_PATH"
)

EXPERIMENT_NAME = os.getenv(
    "EXPERIMENT_NAME"
)