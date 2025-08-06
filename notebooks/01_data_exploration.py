# notebooks/01_data_exploration.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "creditcard.csv")
df = pd.read_csv(DATA_PATH)

# Basic info
print("Shape of dataset:", df.shape)
print("First 5 rows:\n", df.head())

# Check class distribution
class_counts = df['Class'].value_counts()
print("\nClass distribution:\n", class_counts)

# Plot class distribution
plt.figure(figsize=(6, 4))
sns.barplot(x=class_counts.index, y=class_counts.values, hue=class_counts.index, palette="viridis", legend=False)
plt.title("Class Distribution (0 = Legit, 1 = Fraud)")
plt.xlabel("Class")
plt.ylabel("Count")
plt.tight_layout()

# Save plot
os.makedirs("../outputs/visualizations", exist_ok=True)
plt.savefig("../outputs/visualizations/class_distribution.png")
plt.show()

# Summary stats
print("\nSummary statistics:\n", df.describe())
print("Looking for:", os.path.abspath(DATA_PATH))
print("File exists:", os.path.exists(DATA_PATH))
