# EEG-Based Cognitive Confusion Detection

## Overview
This project aims to predict cognitive confusion using EEG-derived spectral features.
Cognitive confusion is closely related to attention, cognitive load, and learning difficulty,
and is a key concept in cognitive neuroscience and educational psychology.

The project was developed as a capstone for the Machine Learning Zoomcamp and focuses on:
- Interpretable EEG features
- Classical machine learning models
- Reproducible pipelines
- Model deployment using Docker

---

## Problem Statement
Detecting when a learner is confused is important for understanding attention and cognitive
processing during learning. EEG provides an objective physiological signal that reflects
changes in neural oscillations associated with mental effort and attentional state.

**Goal:**  
Train a machine learning model to classify whether a subject is confused or not confused
based on EEG spectral features recorded during video-based learning.

---

## Dataset
- Source: *Confused student EEG brainwave dataset* (Kaggle)
- Participants: Students watching MOOC-style educational videos
- Features:
  - EEG spectral band power:
    - Delta (1–3 Hz)
    - Theta (4–7 Hz)
    - Alpha1 (8–11 Hz, lower)
    - Alpha2 (8–11 Hz, higher)
    - Beta1, Beta2
    - Gamma1, Gamma2
  - Proprietary measures:
    - Attention (mental focus)
    - Meditation (calmness)
- Target:
  - Binary confusion label (confused vs not confused)

---


## Exploratory Data Analysis (EDA)

EDA revealed several important characteristics:
- Proprietary features were excluded due to unclear derivation and limited interpretability.
- EEG power features exhibit strong right-skew and heavy tails
- Log transformation significantly stabilizes distributions
- Strong correlations exist between adjacent frequency bands
- Class-conditional distributions show substantial overlap, indicating a challenging classification task
Based on this, we used:
- Log transformation of EEG bands
- Preference for nonlinear tree-based models
---
### Modeling Approach
Problem Formulation
- Task: Binary classification
- Metric: ROC-AUC (robust to class imbalance)
- Validation: Stratified train/validation split + 5-fold cross-validation
Models Evaluated
- Logistic Regression (baseline)
- Random Forest
- XGBoost (final model)
### Results
Model	ROC-AUC
- Logistic Regression	0.56
- Random Forest	0.59
- XGBoost (single split)	0.61
- XGBoost (5-fold CV)	0.60 ± 0.005
XGBoost achieved the best performance with low variance across folds, indicating stable generalization.
---
### Feature Importance
Feature importance analysis from the XGBoost model showed that higher-frequency EEG bands contributed most strongly:
- Beta2
- Gamma2
- Gamma1
- Beta1
consistent with prior findings linking beta–gamma activity to cognitive load and attentional effort.
---

### Limitations
This study has several important limitations:
- Single-channel EEG limits spatial resolution
- No subject-specific normalization
- Labels may contain noise due to task-based annotation
As such, results should be interpreted as feasibility evidence, not a production-ready cognitive state
---

### Deployment
The final model is packaged as a FastAPI web service and deployed using Docker, enabling reproducible inference via a REST API.
Run locally
docker build -t eeg-confusion .
docker run -p 8000:8000 eeg-confusion
Example request
{
  "Delta": 123456,
  "Theta": 23456,
  "Alpha1": 34567,
  "Alpha2": 45678,
  "Beta1": 56789,
  "Beta2": 67890,
  "Gamma1": 78901,
  "Gamma2": 89012
}

---

### Project Structure

├── data/
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_modeling.ipynb
├── src/
│   ├── train.py
│   ├── predict.py
│   └── serve.py
├── model/
│   └── xgb_model.bin
├── Dockerfile
├── requirements.txt
└── README.md


## Future Work
- Subject-specific modeling
- Time-resolved confusion prediction
- Multimodal integration (EEG + video or eye-tracking)
- Deployment using Kubernetes or serverless inference

---



