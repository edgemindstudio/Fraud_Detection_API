# app/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List
import joblib
import numpy as np
import os

app = FastAPI(
    title="Fraud Detection API",
    description="A REST API to predict fraudulent transactions using a trained Random Forest model.",
    version="1.0.0",
)

# ================================
# CORS – restrict to your frontend (and localhost for dev)
# ================================
FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "http://localhost:8501",  # fallback for local Streamlit
)
ALLOWED_ORIGINS = [
    FRONTEND_URL,
    "http://localhost:8501",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================================
# Load the trained model
# ================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model", "RandomForest.pkl")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

try:
    model = joblib.load(model_path)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}") from e

# ================================
# Schemas
# ================================
class Transaction(BaseModel):
    # Enforce exactly 30 floats
    features: List[float] = Field(..., min_length=30, max_length=30, description="30 scaled feature values")

class PredictionResponse(BaseModel):
    prediction: int
    fraud_probability: float
    is_fraud: str

# ================================
# Endpoints
# ================================
@app.post("/predict", response_model=PredictionResponse)
def predict(transaction: Transaction):
    try:
        data = np.array(transaction.features, dtype=float).reshape(1, -1)
    except Exception:
        raise HTTPException(status_code=422, detail="Features must be numeric.")

    pred = int(model.predict(data)[0])
    prob = float(model.predict_proba(data)[0][1])

    return {
        "prediction": pred,
        "fraud_probability": round(prob, 4),
        "is_fraud": "Yes" if pred == 1 else "No",
    }

@app.get("/healthz")
def healthz():
    # Simple readiness check for Render health checks
    return {"status": "ok", "model_loaded": True}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fraud Detection API. Go to /docs to test the model."}
