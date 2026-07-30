from app.ai.feature_extractor import extract_features
from app.config import TRAIN_AUDIO_DIR

print("Step 1")

audio_files = list(TRAIN_AUDIO_DIR.glob("*.flac"))

print("Step 2")
print("Total audio files:", len(audio_files))

if len(audio_files) == 0:
    raise Exception("No FLAC files found!")

audio = audio_files[0]

print("Step 3")
print(audio)

print("Step 4")

features = extract_features(audio)

print("Step 5")

print("Feature Length:", len(features))

print(features[:10])