import librosa
import numpy as np


def get_audio_statistics(y, sr):

    duration = librosa.get_duration(
        y=y,
        sr=sr
    )

    rms = np.mean(
        librosa.feature.rms(y=y)
    )

    zcr = np.mean(
        librosa.feature.zero_crossing_rate(y=y)
    )

    centroid = np.mean(
        librosa.feature.spectral_centroid(
            y=y,
            sr=sr
        )
    )

    bandwidth = np.mean(
        librosa.feature.spectral_bandwidth(
            y=y,
            sr=sr
        )
    )

    return {
        "duration": round(float(duration), 2),
        "sample_rate": sr,
        "rms_energy": round(float(rms), 5),
        "zero_crossing_rate": round(float(zcr), 5),
        "spectral_centroid": round(float(centroid), 2),
        "spectral_bandwidth": round(float(bandwidth), 2),
    }