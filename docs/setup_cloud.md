# Cloud Deployment Guide — Fraud Detection API

This guide explains how to deploy the Fraud Detection API and Streamlit frontend to the cloud using **Render** with Docker.

---

## 1. Prerequisites
- A [GitHub](https://github.com) account
- A [Render](https://render.com) account (free tier works for this project)
- This project pushed to a public or private GitHub repository

---

## 2. Deploy Backend API (FastAPI) on Render

1. **Login to Render** and click **"New +" → Web Service**.
2. **Connect your GitHub repo** and select `Fraud_Detection_API`.
3. **Service Name:** `fraud-detection-api` (or any unique name)
4. **Environment:** `Docker`
5. **Root Directory:** `/` (project root)
6. **Dockerfile Path:** `Dockerfile`
7. **Port:** `8000`
8. **Branch:** `main`
9. **Click Create Web Service** — Render will build and deploy your app.

Once deployed, your backend will be live at:
```cpp
https://fraud-detection-api-xxxx.onrender.com
```
Swagger docs will be available at:
```cpp
https://fraud-detection-api-xxxx.onrender.com/docs
```

---

## 3. Deploy Frontend UI (Streamlit) on Render

1. **Login to Render** and click **"New +" → Web Service** again.
2. Select the same GitHub repo.
3. **Service Name:** `fraud-detection-api-frontend`
4. **Environment:** `Docker`
5. **Root Directory:** `/` (project root)
6. **Dockerfile Path:** `Dockerfile.streamlit`
7. **Port:** `8501`
8. **Branch:** `main`
9. **Click Create Web Service** — Render will build and deploy the UI.

Once deployed, your frontend will be live at:
```cpp
https://fraud-detection-api-frontend.onrender.com
```

---

## 4. Enable CORS on the Backend
In `app/main.py` ensure you allow your frontend domain:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://fraud-detection-api-frontend.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
Push the changes to GitHub — Render will redeploy automatically.

## 5. Testing the Live App
- Open your frontend URL (`/`) and enter 30 scaled features.
- The frontend will send a request to the backend `/predict` endpoint and display results in real time.