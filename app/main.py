# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import os

app = FastAPI(
    title="Fraud Detection API",
    description="A REST API to predict fraudulent transactions using a trained Random Forest model.",
    version="1.0.0"
)

# ================================
# Enable CORS (currently allow all, restrict later)
# ================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later replace with ["https://YOUR-UI.onrender.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================================
# Load the trained model
# ================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model", "RandomForest.pkl")  # works in Render
# model_path = os.path.join(os.path.dirname(__file__), "..", "outputs", "RandomForest.pkl")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

model = joblib.load(model_path)

# ================================
# Define the input schema
# ================================
class Transaction(BaseModel):
    features: list  # Must be a list of 30 floats (scaled input features)

# ================================
# Endpoints
# ================================
@app.post("/predict")
def predict(transaction: Transaction):
    if len(transaction.features) != 30:
        return {"error": "Input must be a list of 30 scaled features."}

    data = np.array(transaction.features).reshape(1, -1)
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return {
        "prediction": int(prediction),
        "fraud_probability": round(float(probability), 4),
        "is_fraud": "Yes" if prediction == 1 else "No"
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fraud Detection API. Go to /docs to test the model."}