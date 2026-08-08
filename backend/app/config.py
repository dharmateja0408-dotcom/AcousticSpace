from pathlib import Path

# ==========================================
# Dataset Location
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET_ROOT = PROJECT_ROOT / "dataset" / "LA"

TRAIN_AUDIO_DIR = (
    DATASET_ROOT / "ASVspoof2019_LA_train" / "flac"
)

DEV_AUDIO_DIR = (
    DATASET_ROOT / "ASVspoof2019_LA_dev" / "flac"
)

PROTOCOL_DIR = (
    DATASET_ROOT / "ASVspoof2019_LA_cm_protocols"
)

# ==========================================
# Model Folder
# ==========================================

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

# ==========================================
# Upload Folder
# ==========================================

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# Report Folder
# ==========================================

REPORT_DIR = Path("app/reports")
REPORT_DIR.mkdir(parents=True, exist_ok=True)
