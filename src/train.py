import pandas as pd
import joblib
from pathlib import Path

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

from src.preprocessing import preprocess_features, FEATURES


DATA_PATH = Path("data/EEG_data.csv")
MODEL_PATH = Path("model/xgb_model.bin")


def main():
    # Load dataset
    df = pd.read_csv(DATA_PATH)

    # Target variable
    y = df['predefinedlabel']

    # Preprocess features
    X = preprocess_features(df)

    # Train / validation split
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    # Define model
    model = XGBClassifier(
        n_estimators=300,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="binary:logistic",
        eval_metric="auc",
        random_state=42,
        n_jobs=-1
    )

    # Train
    model.fit(X_train, y_train)

    # Validate
    y_pred = model.predict_proba(X_val)[:, 1]
    auc = roc_auc_score(y_val, y_pred)
    print(f"Validation ROC-AUC: {auc:.4f}")

    # Save model
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
