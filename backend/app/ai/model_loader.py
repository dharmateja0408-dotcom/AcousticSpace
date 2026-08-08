import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "deepfake_detector.pkl"

model = joblib.load(MODEL_PATH)

print(f"Model loaded from: {MODEL_PATH}")
