import librosa


def load_audio(audio_path, sample_rate=16000):
    """
    Load an audio file and resample it to the required sample rate.
    """

    audio, sr = librosa.load(
        audio_path,
        sr=sample_rate
    )

    return audio, sr
