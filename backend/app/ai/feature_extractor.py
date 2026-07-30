import librosa
import numpy as np


def extract_features(audio_path):

    y, sr = librosa.load(audio_path, sr=16000)

    mfcc = librosa.feature.mfcc(
        y=y,
        sr=sr,
        n_mfcc=20
    )

    chroma = librosa.feature.chroma_stft(
        y=y,
        sr=sr
    )

    contrast = librosa.feature.spectral_contrast(
        y=y,
        sr=sr
    )

    centroid = librosa.feature.spectral_centroid(
        y=y,
        sr=sr
    )

    bandwidth = librosa.feature.spectral_bandwidth(
        y=y,
        sr=sr
    )

    rolloff = librosa.feature.spectral_rolloff(
        y=y,
        sr=sr
    )

    zcr = librosa.feature.zero_crossing_rate(y)

    rms = librosa.feature.rms(y=y)

    features = np.hstack([

        np.mean(mfcc, axis=1),

        np.mean(chroma, axis=1),

        np.mean(contrast, axis=1),

        np.mean(centroid),

        np.mean(bandwidth),

        np.mean(rolloff),

        np.mean(zcr),

        np.mean(rms)

    ])

    return features