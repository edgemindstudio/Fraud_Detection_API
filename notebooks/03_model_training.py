# notebooks/03_model_training.py

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix, ConfusionMatrixDisplay, roc_curve, precision_recall_curve
import matplotlib.pyplot as plt
import os
import joblib

# Load data
train = np.load("../outputs/preprocessed/train_data.npz")
test = np.load("../outputs/preprocessed/test_data.npz")
X_train, y_train = train["X"], train["y"]
X_test, y_test = test["X"], test["y"]

# Train models
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42),
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42)
}

results = {}

for name, model in models.items():
    print(f"\n Training {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    auc = roc_auc_score(y_test, y_prob)
    print(f"AUC Score: {auc:.4f}")
    print(classification_report(y_test, y_pred))

    # Save model
    joblib.dump(model, f"../outputs/{name}.pkl")

    # Store results
    results[name] = {"model": model, "y_pred": y_pred, "y_prob": y_prob}

    # Plot Confusion Matrix
    disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred), display_labels=["Legit", "Fraud"])
    disp.plot()
    plt.title(f"{name} - Confusion Matrix")
    plt.savefig(f"../outputs/visualizations/{name}_confusion_matrix.png")
    plt.close()

    # Plot ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.plot(fpr, tpr, label=f"{name} (AUC = {auc:.2f})")

# Final ROC Plot
plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison")
plt.legend()
plt.tight_layout()
plt.savefig("../outputs/visualizations/roc_comparison.png")
plt.show()
