# Model Training — Fraud Detection API

This document explains how the fraud detection machine learning model was trained, evaluated, and saved for deployment.

---

## 1. Objective
The goal was to detect fraudulent credit card transactions using a dataset with **heavy class imbalance**.  
Fraudulent cases are rare, so handling this imbalance was a critical part of model training.

---

## 2. Dataset
- **Source:** `data/creditcard.csv`
- **Rows:** ~284,807 transactions
- **Features:** 30 numerical features (V1–V28 from PCA + `Time` + `Amount`)
- **Target:** `Class` (0 = Legitimate, 1 = Fraud)

---

## 3. Preprocessing
1. **Feature Scaling:**
   - StandardScaler applied to `Time` and `Amount` columns.
   - PCA-transformed features (V1–V28) already scaled.
   
2. **Class Balancing:**
   - Used **SMOTE** (Synthetic Minority Oversampling Technique) from `imbalanced-learn` to oversample fraud cases in the training set.

3. **Train/Test Split:**
   - 80% training, 20% testing split.

---

## 4. Models Evaluated
Two models were trained and evaluated:

| Model               | AUC Score |
| ------------------- | --------- |
| Logistic Regression | 0.9619    |
| Random Forest       | 0.9609    |

---

## 5. Final Model Choice
We selected **Random Forest** for deployment because:
- Competitive AUC score
- Better interpretability for feature importance
- Stable predictions for imbalanced datasets

---

## 6. Training Script / Notebook
The training process is documented in the Jupyter notebook:
- `notebooks/01_data_exploration.py` — Exploratory Data Analysis (EDA)
- `notebooks/02_preprocessing.py` — Preprocessing + SMOTE balancing
- `notebooks/03_model_training.py` — Model training, evaluation, and saving

---

## 7. Model Saving
The final model was saved using `joblib`:
```python
import joblib
joblib.dump(best_model, "outputs/RandomForest.pkl")
```
For deployment on Render, the model file is stored in:
```bash
  app/model/RandomForest.pkl
```
## 8. Key Results
- **Accuracy**: ~94%
- **AUC**: 0.9609
- **Inference Speed**: <200ms per request

## 9. Next Steps
- Experiment with XGBoost or LightGBM
- Tune hyperparameters for improved precision/recall
- Add drift detection for real-world deployment

