# Cognitive Load Prediction from EEG Features
Project Overview
This project aims to predict cognitive load (low vs high) using EEG-derived spectral features. Cognitive load is a fundamental concept in cognitive neuroscience, relevant to attention, working memory, language processing, and human–computer interaction.
Using machine learning, we build a reproducible pipeline that:
. Explores EEG band-power features
. Trains and compares multiple classification models
. Deploys the final model as a REST API using Docker

Problem Statement
Assessing cognitive load traditionally relies on behavioral measures or subjective reporting. EEG provides an objective physiological signal, but manual analysis is time-consuming.

Goal:
Use supervised machine learning to classify low vs high cognitive load from EEG spectral features.

Dataset
Source: Public EEG dataset from Kaggle (datasets section)

Features:
Frequency band power: delta, theta, alpha, beta, gamma
Aggregated across channels

Target:
Cognitive load level (binary classification)
The dataset is small enough for rapid experimentation while remaining representative of real EEG-based cognitive tasks.

Exploratory Data Analysis
. Distribution of EEG band power features
. Correlation analysis between frequency bands
. Class balance inspection
. EDA results informed feature scaling and model selection.

Models Trained
The following models were trained and evaluated:
Model	Description
. Logistic Regression	Baseline linear classifier
. Random Forest	Non-linear ensemble model
. Gradient Boosting	Tuned ensemble model
. (Optional) MLP	Simple neural network

Evaluation Metric
Primary metric: ROC-AUC
Secondary: Accuracy, F1-score
ROC-AUC was selected due to potential class imbalance and interpretability.

Final Model
The best-performing model was selected based on validation ROC-AUC and exported using joblib.

Deployment
The trained model is deployed as a REST API using:
FastAPI for inference
Docker for containerization
Example Request
{
  "delta": 0.45,
  "theta": 0.62,
  "alpha": 0.31,
  "beta": 0.22,
  "gamma": 0.18
}
Example Response
{
  "cognitive_load_probability": 0.81,
  "prediction": "high"
}

Future Work
. Channel-level feature modeling
. Time-resolved cognitive load prediction
. Multimodal integration (speech or eye-tracking)
. Deployment using Kubernetes or serverless inference


