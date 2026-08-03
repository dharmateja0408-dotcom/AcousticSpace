import os
import librosa
import numpy as np
from tqdm import tqdm

# ==============================
# Paths
# ==============================

AUDIO_DIR = "dataset/LA/ASVspoof2019_LA_train/flac"

PROTOCOL_FILE = (
    "dataset/LA/ASVspoof2019_LA_cm_protocols/"
    "ASVspoof2019.LA.cm.train.trn.txt"
)

FEATURE_DIR = "dataset/processed/features"
LABEL_DIR = "dataset/processed/labels"

os.makedirs(FEATURE_DIR, exist_ok=True)
os.makedirs(LABEL_DIR, exist_ok=True)

# ==============================
# Read Protocol File
# ==============================

samples = []

with open(PROTOCOL_FILE, "r") as f:
    for line in f:
        parts = line.strip().split()

        file_id = parts[1]
        label = parts[-1]

        samples.append((file_id, label))

print(f"Total samples: {len(samples)}")

# ==============================
# Process Audio Files
# ==============================

MAX_LEN = 100

for file_id, label in tqdm(samples):

    audio_path = os.path.join(
        AUDIO_DIR,
        file_id + ".flac"
    )

    audio, sr = librosa.load(audio_path, sr=16000)

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=40
    )

    # Pad or truncate MFCC to fixed length
    if mfcc.shape[1] < MAX_LEN:

        pad_width = MAX_LEN - mfcc.shape[1]

        mfcc = np.pad(
            mfcc,
            ((0, 0), (0, pad_width)),
            mode="constant"
        )

    else:

        mfcc = mfcc[:, :MAX_LEN]

    feature_path = os.path.join(
        FEATURE_DIR,
        file_id + ".npy"
    )

    label_path = os.path.join(
        LABEL_DIR,
        file_id + ".npy"
    )

    np.save(feature_path, mfcc)

    np.save(
        label_path,
        np.array(
            1 if label == "bonafide" else 0,
            dtype=np.int64
        )
    )

print("\nFeature extraction completed successfully!")