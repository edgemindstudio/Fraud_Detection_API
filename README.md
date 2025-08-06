# 🛡️ Fraud Detection API

A complete machine learning pipeline for detecting fraudulent credit card transactions — trained, evaluated, and deployed with a FastAPI backend.

## 🚀 Project Overview

This project:
- Trains a fraud detection model using credit card transaction data
- Handles heavy class imbalance using SMOTE
- Evaluates multiple models (Random Forest, Logistic Regression)
- Deploys a trained model as a REST API using FastAPI
- Returns live fraud prediction via `/predict` endpoint

## 📁 Folder Structure

```kotlin
FraudDetection/
├── app/
│   └── main.py
├── data/
│   └── creditcard.csv
├── notebooks/
│   ├── 01_data_exploration.py
│   ├── 02_preprocessing.py
│   └── 03_model_training.py
├── outputs/
│   ├── RandomForest.pkl
│   ├── LogisticRegression.pkl
│   ├── preprocessed/
│   │   ├── train_data.npz
│   │   └── test_data.npz
│   └── visualizations/
│       ├── class_distribution.png
│       ├── roc_comparison.png
│       ├── LogisticRegression_confusion_matrix.png
│       └── RandomForest_confusion_matrix.png
├── requirements.txt
├── locked_requirements.txt
└── README.md 
```

```kotlin
FraudDetection/
├── app/# FastAPI backend
├── data/# Original dataset (creditcard.csv)
├── notebooks/# EDA, preprocessing, model training
├── outputs/# Saved models, plots, test/train data
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```

## ⚙️ How to Use

### 1. Clone the repository

```bash
  git clone https://github.com/YOUR_USERNAME/FraudDetection.git
  cd FraudDetection
```
### 2. Create and activate virtual environment

```bash
  python3 -m venv .venv
  source .venv/bin/activate  # or .venv\Scripts\activate on Windows
  pip install -r requirements.txt
```

### 3. Launch the API

```bash
  uvicorn app.main:app --reload
```

Then visit 👉 http://127.0.0.1:8000/docs to test the API.

## 🔍 Example API Request

### POST /predict

```json
{
  "features": [
    -1.359, -0.072, 2.536, 1.378, -0.338, 0.462, 0.239, 0.099, 0.134, -0.021,
    0.206, 0.502, 0.219, -0.018, 0.215, 0.128, 0.098, 0.018, 0.277, 0.404,
    0.038, 0.039, 0.015, 0.015, -0.005, 0.178, 0.507, 0.119, -0.066, 0.028
  ]
}
```

### Response

```json
{
  "prediction": 0,
  "fraud_probability": 0.0027,
  "is_fraud": "No"
}
```

## Models Used

----------------
| Model               | AUC Score |
| ------------------- | --------- |
| Logistic Regression | 0.9619    |
| Random Forest       | 0.9609    |
----------------

## 📊 Visuals
- Class distribution before & after SMOTE
- Confusion matrices
- ROC curve comparison
----------------

## 🛠️ Tech Stack
- Python, NumPy, pandas
- scikit-learn, imbalanced-learn
- FastAPI, Uvicorn
- Matplotlib, Seaborn
- SMOTE (for class balancing)
----------------

## 📘 Author

- **Bruno Fonkeng**
- [Github](https://github.com/edgemindstudio) | [LinkedIn](https://www.linkedin.com/in/edgemindstudio/)

---

### 📄 1.3. Confirm `requirements.txt`

If not already updated, run:
```bash
    pip freeze > requirements.txt
```