import numpy as np

FEATURES = [
    "Delta",
    "Theta",
    "Alpha1",
    "Alpha2",
    "Beta1",
    "Beta2",
    "Gamma1",
    "Gamma2"
]

def preprocess_features(df):
    """
    Applies frozen preprocessing steps to EEG features.
    """
    X = df[FEATURES].copy()

    # Log-transform EEG power features
    for col in FEATURES:
        X[col] = np.log1p(X[col])

    return X
