import time
import joblib
import numpy as np
import librosa
from pathlib import Path

from app.ai.feature_extractor import extract_features

MODEL_PATH = Path("models/deepfake_detector.pkl")

# Load model once at startup
model = joblib.load(MODEL_PATH)


def predict_audio(audio_path):

    start = time.time()

    # Load audio metadata
    audio, sr = librosa.load(audio_path, sr=None)

    duration = round(len(audio) / sr, 2)

    features = extract_features(audio_path)
    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]

    confidence = round(
        float(np.max(probabilities)) * 100,
        2
    )

    analysis_time = round(
        time.time() - start,
        3
    )

    label = "Real" if prediction == 0 else "Spoof"

    # Risk Level
    if confidence < 60:
        risk = "Low"
    elif confidence < 85:
        risk = "Medium"
    else:
        risk = "High"

    # AI Recommendation
    if label == "Spoof":
        recommendation = (
            "This recording contains characteristics "
            "commonly associated with synthetic or manipulated speech. "
            "Manual verification is recommended."
        )
    else:
        recommendation = (
            "No significant spoofing characteristics were detected. "
            "The recording appears genuine according to the current model."
        )

    return {

        "prediction": label,

        "confidence": confidence,

        "risk": risk,

        "recommendation": recommendation,

        "duration": duration,

        "sample_rate": sr,

        "analysis_time": analysis_time
    }