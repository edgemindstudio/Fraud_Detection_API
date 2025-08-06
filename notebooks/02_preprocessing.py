# notebooks/02_preprocessing.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import os

# Load dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "creditcard.csv")
df = pd.read_csv(DATA_PATH)

# Drop duplicates
df = df.drop_duplicates()

# Scale 'Time' and 'Amount'
scaler = StandardScaler()
df[['scaled_time', 'scaled_amount']] = scaler.fit_transform(df[['Time', 'Amount']])
df.drop(['Time', 'Amount'], axis=1, inplace=True)

# Split features and label
X = df.drop('Class', axis=1)
y = df['Class']

# Split train/test with stratified sampling
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Handle class imbalance using SMOTE on training set only
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Save to outputs
output_dir = "../outputs/preprocessed"
os.makedirs(output_dir, exist_ok=True)
np.savez_compressed(os.path.join(output_dir, "train_data.npz"),
                    X=X_train_resampled, y=y_train_resampled)
np.savez_compressed(os.path.join(output_dir, "test_data.npz"),
                    X=X_test, y=y_test)

# Print stats
print("Original class distribution:")
print(y.value_counts())
print("\nAfter SMOTE on training data:")
print(pd.Series(y_train_resampled).value_counts())
print(f"\nSaved: train_data.npz and test_data.npz to {output_dir}")
