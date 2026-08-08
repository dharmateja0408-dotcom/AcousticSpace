import time
import numpy as np
import pandas as pd

from app.ai.preprocessing import load_audio
from app.ai.feature_extractor import extract_features
from app.ai.model_loader import model
from app.ai.statistics import get_audio_statistics


def predict_audio(audio_path):

    start = time.time()

    # Load and preprocess audio
    audio, sr = load_audio(audio_path)

    # Extract features
    features = extract_features(audio_path)

    # Use the same feature names used during Random Forest training
    feature_names = [str(i) for i in range(len(features))]

    features_df = pd.DataFrame(
        [features],
        columns=feature_names
    )

    # Model prediction
    prediction = model.predict(features_df)[0]

    probabilities = model.predict_proba(features_df)[0]

    confidence = round(
        float(np.max(probabilities)) * 100,
        2
    )

    # Label
    label = "Real" if prediction == 0 else "Spoof"

    # Risk level
    if confidence < 60:
        risk = "Low"
    elif confidence < 85:
        risk = "Medium"
    else:
        risk = "High"

    # Audio statistics
    statistics = get_audio_statistics(audio_path)

    # Recommendation
    if label == "Spoof":
        recommendation = (
            "This recording contains characteristics commonly "
            "associated with synthetic or manipulated speech. "
            "Manual verification is recommended."
        )
    else:
        recommendation = (
            "No significant spoofing characteristics were detected. "
            "The recording appears genuine according to the current model."
        )

    analysis_time = round(
        time.time() - start,
        3
    )

    return {
        "prediction": label,
        "confidence": confidence,
        "risk": risk,
        "recommendation": recommendation,
        "duration": statistics["duration"],
        "sample_rate": statistics["sample_rate"],
        "rms_energy": statistics["rms_energy"],
        "zero_crossing_rate": statistics["zero_crossing_rate"],
        "spectral_centroid": statistics["spectral_centroid"],
        "spectral_bandwidth": statistics["spectral_bandwidth"],
        "analysis_time": analysis_time
    }
