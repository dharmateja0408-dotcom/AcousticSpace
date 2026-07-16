import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def process_audio(audio_path):
    # Load audio
    audio, sample_rate = librosa.load(audio_path)

    print("========== Audio Information ==========")
    print("Sample Rate:", sample_rate)
    print("Number of Samples:", len(audio))

    duration = librosa.get_duration(y=audio, sr=sample_rate)
    print("Duration:", round(duration, 3), "seconds")

    # -----------------------------
    # Waveform
    # -----------------------------
    plt.figure(figsize=(12, 4))

    librosa.display.waveshow(audio, sr=sample_rate)

    plt.title("Audio Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.savefig("waveform.png")
    plt.close()

    print("✅ Waveform saved as waveform.png")

    # -----------------------------
    # Mel Spectrogram
    # -----------------------------
    spectrogram = librosa.feature.melspectrogram(
        y=audio,
        sr=sample_rate
    )

    spectrogram_db = librosa.power_to_db(
        spectrogram,
        ref=np.max
    )

    plt.figure(figsize=(10, 4))

    librosa.display.specshow(
        spectrogram_db,
        sr=sample_rate,
        x_axis="time",
        y_axis="mel"
    )

    plt.colorbar(format="%+2.0f dB")
    plt.title("Mel Spectrogram")

    plt.tight_layout()

    plt.savefig("spectrogram.png")
    plt.close()

    print("✅ Spectrogram saved as spectrogram.png")

    # -----------------------------
    # MFCC Features
    # -----------------------------
    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sample_rate,
        n_mfcc=13
    )

    print("MFCC Shape:", mfcc.shape)

    print("========== Processing Completed ==========")


if __name__ == "__main__":
    process_audio("dataset/sample/0_george_0.wav")