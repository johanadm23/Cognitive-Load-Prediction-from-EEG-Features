import joblib
import pandas as pd
from pathlib import Path

from src.preprocessing import preprocess_features, FEATURES



MODEL_PATH = Path("model/xgb_model.bin")


def predict_confusion(features: dict) -> float:
    """
    Predict probability of cognitive confusion.

    Parameters
    ----------
    features : dict
        Dictionary with EEG band powers.

    Returns
    -------
    float
        Probability of confusion.
    """
    # Convert input to DataFrame
    df = pd.DataFrame([features])

    # Apply frozen preprocessing
    X = preprocess_features(df)

    # Load model
    model = joblib.load(MODEL_PATH)

    # Predict probability
    prob = model.predict_proba(X)[0, 1]

    return float(prob)


if __name__ == "__main__":
    # Example test
    example = {
        "Delta": 123456,
        "Theta": 23456,
        "Alpha1": 34567,
        "Alpha2": 45678,
        "Beta1": 56789,
        "Beta2": 67890,
        "Gamma1": 78901,
        "Gamma2": 89012
    }

    p = predict_confusion(example)
    print("Confusion probability:", p)
