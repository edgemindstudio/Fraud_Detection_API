# Docker Setup Guide — Fraud Detection API

This guide explains how to build and run the **Fraud Detection API** using Docker.

---

## 1. Prerequisites
- Install **Docker** on your machine:
  - [Docker Desktop](https://www.docker.com/products/docker-desktop/) (macOS/Windows)
  - `sudo apt install docker.io` (Linux)
- Clone the project repository:
```bash
  git clone https://github.com/edgemindstudio/Fraud_Detection_API.git
  cd Fraud_Detection_API
```
## 2. Backend (FastAPI) — Docker
Build the Docker Image
```bash
    docker build -t fraud-detection-api -f Dockerfile .
```
**Run the Container**
```bash
    docker run -d -p 8000:8000 fraud-detection-api
```
The API will be available at:
```cpp
    http://127.0.0.1:8000
```
Swagger docs:
```arduino
    http://127.0.0.1:8000/docs
```

## 3. Frontend (Streamlit) — Docker
If you want to run the Streamlit UI in Docker, use the Dockerfile.streamlit:
**Build the Frontend Image**
```bash
    docker build -t fraud-detection-frontend -f Dockerfile.streamlit .
```
**Run the Container**
```bash
    docker run -d -p 8501:8501 fraud-detection-frontend
```
The Streamlit UI will be available at:
```cpp
    http://127.0.0.1:8501
```

## 4. Running Both Together
If you want both backend and frontend running locally in Docker:
```bash
    # Terminal 1 — Backend
    docker run -d -p 8000:8000 fraud-detection-api

    # Terminal 2 — Frontend
    docker run -d -p 8501:8501 fraud-detection-frontend
```
