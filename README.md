# Cognitive Load Prediction from EEG Features

## Overview
This project predicts cognitive load (low vs high) using EEG derived spectral features.
Cognitive load is a key concept in cognitive neuroscience, relevant to attention, working memory,
and language processing.

The project was developed as a capstone for the Machine Learning Zoomcamp and focuses on
reproducibility, interpretability, and deployment.

---

## Problem Statement
Cognitive load is traditionally assessed using behavioral measures or self-reports.
EEG provides an objective physiological signal, but manual analysis is time consuming.

**Goal:**  
Train a machine learning model to classify low vs high cognitive load from EEG band-power features.

---

## Dataset
- Source: Public EEG dataset from Kaggle (datasets section)
- Features: Delta, Theta, Alpha, Beta, Gamma band power
- Target: Binary cognitive load label (derived from mental state indicators)

---

## Exploratory Data Analysis
EDA includes:
- Feature distributions
- Correlation analysis between EEG bands
- Class balance inspection

---

## Models
- Logistic Regression (baseline)
- Random Forest
- Gradient Boosting
- (Optional) Neural Network (MLP)

---

## Evaluation
- Primary metric: ROC-AUC
- Secondary metrics: Accuracy, F1-score

---

## Deployment
The final model is deployed as a REST API using FastAPI and Docker.

---

## Project Structure
cognitive-load-eeg-ml/
- data/
- notebooks/
- src/
- models/
- Dockerfile
- README.md
- requirements.txt

---

## Reproducibility
- Fixed random seeds
- Version-pinned dependencies
- Training and inference are separated



