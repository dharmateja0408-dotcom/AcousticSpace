from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import torch
import torch.nn.functional as F
import librosa
import numpy as np
import tempfile
import os

from model import CNNClassifier

app = FastAPI()

# =====================================
# Enable CORS
# =====================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================
# Load Trained Model
# =====================================
model = CNNClassifier()

model.load_state_dict(
    torch.load(
        "models/baseline_cnn.pth",
        map_location=torch.device("cpu")
    )
)

model.eval()

# =====================================
# Home Route
# =====================================
@app.get("/")
def home():
    return {
        "message": "AcousticSpace API Running"
    }

# =====================================
# Prediction Route
# =====================================
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Save uploaded file temporarily
    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:

        temp.write(await file.read())

        temp_path = temp.name

    # Load audio
    audio, sr = librosa.load(
        temp_path,
        sr=16000
    )

    # Delete temp file
    os.remove(temp_path)

    # Extract MFCC
    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=40
    )

    # Match training preprocessing
    MAX_LEN = 100

    if mfcc.shape[1] < MAX_LEN:

        pad = MAX_LEN - mfcc.shape[1]

        mfcc = np.pad(
            mfcc,
            ((0, 0), (0, pad)),
            mode="constant"
        )

    else:

        mfcc = mfcc[:, :MAX_LEN]

    # Convert to tensor
    feature = torch.tensor(
        mfcc,
        dtype=torch.float32
    )

    feature = feature.unsqueeze(0)
    feature = feature.unsqueeze(0)

    # Prediction
    with torch.no_grad():

        output = model(feature)

        probabilities = F.softmax(output, dim=1)

        confidence, predicted = torch.max(probabilities, dim=1)

    prediction = (
        "Bonafide"
        if predicted.item() == 1
        else "Spoof"
    )

    return {
        "filename": file.filename,
        "prediction": prediction,
        "confidence": round(confidence.item() * 100, 2)
    }


# =====================================
# Run Server
# =====================================
if __name__ == "__main__":

    uvicorn.run(
        "predict:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )