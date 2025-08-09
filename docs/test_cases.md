# Test Cases — Fraud Detection API

This document describes how to test the `/predict` endpoint locally and on the live Render deployment.

---

## 1. Local Testing (FastAPI Running Locally)

### Prerequisites
- API running locally:
```bash
  uvicorn app.main:app --reload
```
- Local URL: http://127.0.0.1:8000

Test with `curl`
```bash
  curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "features": [
      -1.359, -0.072, 2.536, 1.378, -0.338, 0.462, 0.239, 0.099, 0.134, -0.021,
      0.206, 0.502, 0.219, -0.018, 0.215, 0.128, 0.098, 0.018, 0.277, 0.404,
      0.038, 0.039, 0.015, 0.015, -0.005, 0.178, 0.507, 0.119, -0.066, 0.028
    ]
  }'
```
### Expected Response

```json
{
  "prediction": 0,
  "fraud_probability": 0.0027,
  "is_fraud": "No"
}
```
## 2. Live Testing (Render Deployment)
**API URL**

`https://fraud-detection-api-27ae.onrender.com/predict`

Test with `curl`
```bash
  curl -X POST "https://fraud-detection-api-27ae.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "features": [
      -1.359, -0.072, 2.536, 1.378, -0.338, 0.462, 0.239, 0.099, 0.134, -0.021,
      0.206, 0.502, 0.219, -0.018, 0.215, 0.128, 0.098, 0.018, 0.277, 0.404,
      0.038, 0.039, 0.015, 0.015, -0.005, 0.178, 0.507, 0.119, -0.066, 0.028
    ]
  }'
```
### Expected Response

```json
{
  "prediction": 0,
  "fraud_probability": 0.0027,
  "is_fraud": "No"
}
```

## 3. Testing with Python (requests library)

Create a test_api.py file:

```python
import requests

url = "https://fraud-detection-api-27ae.onrender.com/predict"

payload = {
    "features": [
        -1.359, -0.072, 2.536, 1.378, -0.338, 0.462, 0.239, 0.099, 0.134, -0.021,
        0.206, 0.502, 0.219, -0.018, 0.215, 0.128, 0.098, 0.018, 0.277, 0.404,
        0.038, 0.039, 0.015, 0.015, -0.005, 0.178, 0.507, 0.119, -0.066, 0.028
    ]
}

response = requests.post(url, json=payload)
print(response.json())
```
Run:


```bash
  python test_api.py
```