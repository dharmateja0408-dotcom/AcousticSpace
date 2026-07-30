from app.config import (
    TRAIN_AUDIO_DIR,
    DEV_AUDIO_DIR,
    PROTOCOL_DIR,
)

print("Train Folder:", TRAIN_AUDIO_DIR)
print("Dev Folder:", DEV_AUDIO_DIR)
print("Protocol Folder:", PROTOCOL_DIR)

print()

print("Train files:", len(list(TRAIN_AUDIO_DIR.glob("*.flac"))))
print("Dev files:", len(list(DEV_AUDIO_DIR.glob("*.flac"))))