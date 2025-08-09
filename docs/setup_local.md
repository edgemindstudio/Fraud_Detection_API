# Local Setup Guide — Fraud Detection API

This guide explains how to set up and run the **Fraud Detection API** locally on your machine.

---

## 1. Clone the Repository
```bash
    git clone https://github.com/edgemindstudio/Fraud_Detection_API.git
    cd Fraud_Detection_API
```
## 2. Create a Virtual Environment
It’s recommended to use a Python virtual environment to keep dependencies isolated.
```bash
    python3 -m venv .venv
    source .venv/bin/activate  # macOS/Linux
    # OR
    .venv\Scripts\activate     # Windows
```
## 3. Install Dependencies
Install the backend dependencies from requirements.txt:
```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    
    # If you also want to run the Streamlit frontend locally:
    pip install -r requirements_frontend.txt
```
## 4. Ensure Model File Exists
The trained model should be located at:
```bash
    app/model/RandomForest.pkl
```
If missing, retrain it using the notebook in notebooks/03_model_training.py.

## 5. Run the FastAPI Backend
From the project root, run:
```bash
    uvicorn app.main:app --reload
```
By default, the API will start at:
```cpp
http://127.0.0.1:8000
```
## 6. Test API in the Browser
Visit:
```arduino
http://127.0.0.1:8000/docs
```
You’ll see the Swagger UI where you can test the /predict endpoint.

## 7. (Optional) Run the Streamlit Frontend
From the project root:
```bash
  streamlit run frontend/streamlit_app.py
```
This will open the UI in your default browser, allowing you to enter transaction features and view predictions.