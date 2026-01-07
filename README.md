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

## Exploratory Data Analysis
EDA includes:
- Distribution analysis of EEG band power features
- Comparison of EEG features between confused and non-confused states
- Correlation analysis across frequency bands
- Class balance inspection

---

## Models
The following models were trained and compared:
- Logistic Regression (baseline)
- Random Forest
- Gradient Boosting
- (Optional) Multi-layer Perceptron (neural network)

---

## Evaluation
- Primary metric: ROC-AUC
- Secondary metrics: Accuracy, F1-score

ROC-AUC was selected due to potential class imbalance and its robustness for binary
classification.

---

## Deployment
The final model is deployed as a REST API using:
- FastAPI for inference
- Docker for containerization

The API accepts EEG feature values and returns the probability of cognitive confusion.

---

## Reproducibility
- Fixed random seeds
- Version-pinned dependencies
- Training and inference separated into scripts

---

## Project Structure
cognitive-load-eeg-ml/
—— data/
   —— raw/
   —— processed/
—— notebooks/
—— src/
—— models/
—— Dockerfile
—— README.md
—— requirements.txt


---

## Future Work
- Subject-specific modeling
- Time-resolved confusion prediction
- Multimodal integration (EEG + video or eye-tracking)
- Deployment using Kubernetes or serverless inference

---



