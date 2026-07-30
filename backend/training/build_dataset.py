




import pandas as pd
from pathlib import Path
from tqdm import tqdm

from app.ai.dataset import load_train_protocol
from app.ai.feature_extractor import extract_features
from app.config import TRAIN_AUDIO_DIR


def build_dataset():

    protocol = load_train_protocol()

    X = []
    y = []

    print("Starting feature extraction...\n")

    for _, row in tqdm(protocol.iterrows(), total=len(protocol)):

        audio_path = TRAIN_AUDIO_DIR / f"{row['filename']}.flac"

        if not audio_path.exists():
            continue

        try:

            features = extract_features(audio_path)

            X.append(features)

            y.append(
                0 if row["label"] == "bonafide" else 1
            )

        except Exception as e:
            print(f"Skipping {audio_path.name}: {e}")

    df = pd.DataFrame(X)

    df["label"] = y

    output = Path("training/features.csv")

    df.to_csv(output, index=False)

    print("\nDataset Created Successfully!")

    print(df.head())

    print(f"\nSaved to {output}")


if __name__ == "__main__":
    build_dataset()