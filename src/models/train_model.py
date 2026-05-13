import pandas as pd
import mlflow
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error, root_mean_squared_error, r2_score
)

from src.config import (
    MLFLOW_TRACKING_URI,
    EXPERIMENT_NAME
)

DATA_PATH = Path("data/processed/featured_housing.csv")
MODEL_PATH = Path("models/trained/random_forest_model.pkl")

def train_model():
    # ---------
    # Load data
    # ---------

    df = pd.read_csv(DATA_PATH)

    # example target:
    TARGET_COLUMN = "price"

    X = df.drop(columns= [TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    # Keep only numeric for simplicity (Encoder can be added later)
    X = X.select_dtypes(include=["number"])

    # -----
    # Split
    # -----

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 42, test_size=0.2)

    # -------------
    # ML flow setup
    # -------------
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)

    # ---------------------
    # Start experiment run:
    # ---------------------

    with mlflow.start_run():

        # Model 
        model = RandomForestRegressor(
            n_estimators=100,
            max_depth= 10,
            random_state= 42
        )

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        rmse = root_mean_squared_error(
            y_test, predictions
        )


        # --------------
        # Log parameters
        # --------------

        mlflow.log_param("model_type", "RandomForest")

        mlflow.log_param("n_estimater", 100)

        mlflow.log_param("max_depth", 10)

        # -----------
        # Log Metrics
        # -----------

        mlflow.log_metric("rmse", rmse)

        # ----------
        # Save model
        # ----------

        MODEL_PATH.parent.mkdir(
            parents= True,
            exist_ok= True
        )

        joblib.dump(model, MODEL_PATH)

        # ------------
        # Log artifact
        # ------------

        mlflow.log_artifact(MODEL_PATH)

        print(f"RMSE: {rmse}")

        print("Training completed!")

if __name__ == "__main__":
    train_model()

