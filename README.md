# 🛡️ Fraud Detection API

A complete end-to-end machine learning pipeline for detecting fraudulent credit card transactions — trained, evaluated, and deployed using a **FastAPI** backend and live **Dockerized API** hosted on **Render**.
## 🚀 Project Overview

This project:
- Trains a fraud detection model on real-world credit card transaction data
- Handles heavy class imbalance using **SMOTE**
- Evaluates multiple models (Random Forest, Logistic Regression)
- Exports the best model (RandomForest.pkl)
- Deploys a **FastAPI**-powered REST API using Docker + Render
- Accepts 30 scaled features and returns live fraud predictions via the /predict endpoint

---
## 🌐 Live Demo
👉 fraud-detection-api-27ae.onrender.com/docs
Try the /predict endpoint directly from the Swagger UI.
---
## 📁 Folder Structure

```kotlin
FraudDetection/
├── app/                # FastAPI backend
│   └── main.py
│   └── model           # Deployed model storage
├── data/
│   └── creditcard.csv
├── notebooks/          # EDA, preprocessing, training
│   ├── 01_data_exploration.py
│   ├── 02_preprocessing.py
│   └── 03_model_training.py
├── outputs/            # Model evaluation outputs
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
├── requirements.txt     # Core dependencies
├── Dockerfile           # Containerized deployment
└── README.md            # Documentation
```

## ⚙️ How to Use

### 1. Clone the repository

```bash
   git clone https://github.com/YOUR_USERNAME/FraudDetection.git
   cd Fraud_Detection_API
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

Then visit 👉 http://127.0.0.1:8000/docs in your browser to test the API.

---
## 📡 Render Deployment (Dockerized)
The API is deployed live using Render + Docker. No local host or server is required to be running after deployment.

---
## 🟢 Public Endpoint:
https://fraud-detection-api-27ae.onrender.com/predict

---

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
- **Backend**: FastAPI, Uvicorn
- **ML Libraries**: scikit-learn, imbalanced-learn
- **Data**: pandas, NumPy
- **Deployment**: Docker, Render
- **Visualization**: Matplotlib, Seaborn
- **SMOTE** (for class balancing)
----------------

## 📘 Author

- **Bruno Fonkeng**
- [Github](https://github.com/edgemindstudio) | [LinkedIn](https://www.linkedin.com/in/edgemindstudio/)

---
## 📄 Version Info

- API Version: 1.0.0
- OpenAPI Spec: 3.1
- Python Version: 3.10
- Docker-based Deployment

---

### 📄 Dependency Locking

If not already updated, run:
```bash
    pip freeze > requirements.txt