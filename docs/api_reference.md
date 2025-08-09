# API Reference — Fraud Detection API

This document describes all available API endpoints, their request/response formats, and example usage.

---

## Base URL
- **Backend API (FastAPI):** https://fraud-detection-api-27ae.onrender.com  
- **Swagger Docs:** https://fraud-detection-api-27ae.onrender.com/docs

---

## 1. `GET /`
### Description
Health check endpoint — confirms the API is live.

### Response
```json
{
  "message": "Welcome to the Fraud Detection API. Go to /docs to test the model."
}
```

## 2. `POST /predict`
### Description
Predict whether a transaction is fraudulent based on 30 scaled numerical features.

### Request Body
- **Content-Type**: `application/json`
- **Parameters**:
  - `features`: List of exactly 30 float values (scaled features)
### Example Request

```json
{
  "features": [
    -1.359, -0.072, 2.536, 1.378, -0.338, 0.462, 0.239, 0.099, 0.134, -0.021,
    0.206, 0.502, 0.219, -0.018, 0.215, 0.128, 0.098, 0.018, 0.277, 0.404,
    0.038, 0.039, 0.015, 0.015, -0.005, 0.178, 0.507, 0.119, -0.066, 0.028
  ]
}
```
### Example Successful Response

```json
{
  "prediction": 0,
  "fraud_probability": 0.0027,
  "is_fraud": "No"
}
```

### Example Error Response
If the input does not contain exactly 30 features:
```json
{
  "error": "Input must be a list of 30 scaled features."
}
```

## 3. CORS Configuration
The API is configured to accept requests from the frontend:

```pycon
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://fraud-detection-api-frontend.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
## 4. Frontend UI
For a user-friendly way to interact with this API:
- **Streamlit UI**: https://fraud-detection-api-frontend.onrender.com
The UI sends a POST request to `/predict` and displays:
- Prediction (Fraud / No Fraud)
- Fraud Probability (%)

