from fastapi import FastAPI
from pydantic import BaseModel

from predict import predict_confusion
from preprocessing import FEATURES


app = FastAPI(title="EEG Confusion Detection API")


class EEGFeatures(BaseModel):
    Delta: float
    Theta: float
    Alpha1: float
    Alpha2: float
    Beta1: float
    Beta2: float
    Gamma1: float
    Gamma2: float


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(features: EEGFeatures):
    prob = predict_confusion(features.dict())
    return {
        "confusion_probability": prob
    }
