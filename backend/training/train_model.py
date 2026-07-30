import joblib
import pandas as pd

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

print("Loading Dataset...")

df = pd.read_csv("training/features.csv")

X = df.drop("label", axis=1)

y = df["label"]

print(f"Dataset Shape: {df.shape}")

print("\nSplitting Dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("Training Random Forest...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1,
)

model.fit(X_train, y_train)

print("\nMaking Predictions...")

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"\nAccuracy: {accuracy:.4f}")

print("\nClassification Report")

print(classification_report(y_test, predictions))

print("\nConfusion Matrix")

print(confusion_matrix(y_test, predictions))

Path("models").mkdir(exist_ok=True)

joblib.dump(
    model,
    "models/deepfake_detector.pkl"
)

print("\nModel Saved Successfully!")

print("models/deepfake_detector.pkl")