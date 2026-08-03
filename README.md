# AcousticSpace
Deepfake Audio Detection Internship Project

# 🎤 AcousticSpace

AcousticSpace is a deepfake voice detection project developed as part of an internship. The project aims to detect whether an uploaded audio file is genuine or AI-generated using machine learning and audio signal processing techniques.

---

## 📌 Project Overview

The project consists of two main parts:

- **Backend:** FastAPI, Python, Librosa, PyTorch
- **Frontend:** React, TypeScript, Vite

The backend processes uploaded audio files and extracts important audio features, while the frontend provides an intuitive dashboard for users to upload audio and view analysis results.

---

## 🚀 Features

### Backend

- FastAPI server setup
- Audio preprocessing using Librosa
- Waveform generation
- Mel Spectrogram generation
- MFCC feature extraction
- Sample rate detection
- Audio duration calculation

### Frontend

- React + TypeScript application
- Audio upload component
- Static dashboard layout
- Responsive user interface

---

## 🛠️ Technologies Used

### Backend

- Python 3.9+
- FastAPI
- Librosa
- NumPy
- Matplotlib
- SoundFile
- PyTorch *(to be integrated in upcoming phases)*

### Frontend

- React
- TypeScript
- Vite
- HTML5
- CSS3

---

## 📂 Project Structure

```text
AcousticSpace
│
├── backend
│   ├── app.py
│   ├── audio_processing.py
│   ├── model.py
│   ├── rir.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── vite.config.ts
│
├── dataset
│   ├── sample
│   └── processed
│
├── docs
│   └── dataset_info.md
│
├── outputs
│   ├── waveform.png
│   └── spectrogram.png
│
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/dharmateja0408-dotcom/AcousticSpace.git
```

```bash
cd AcousticSpace
```

---

## Backend Setup

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Start the FastAPI server:

```bash
uvicorn backend.app:app --reload
```

---

## Frontend Setup

Navigate to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open your browser and visit:

```text
http://localhost:5173
```

---

## Current Progress

### ✅ Week 1 Completed

- FastAPI setup
- React setup
- Dataset preparation
- Audio preprocessing
- Waveform generation
- Mel Spectrogram generation
- MFCC feature extraction
- Audio upload interface
- Static dashboard

---

## Upcoming Features

- Upload audio directly from the frontend
- Backend API integration
- Machine learning model integration
- Deepfake voice prediction
- Confidence score display
- Interactive dashboard
- Audio history
- Visualization improvements

---

## Example Output

```text
========== Audio Information ==========
Sample Rate: 22050
Number of Samples: 6571
Duration: 0.298 seconds

Waveform saved successfully
Spectrogram saved successfully

MFCC Shape: (13, 13)

========== Processing Completed ==========
```

---

## Future Scope

The project will be extended to include:

- Deepfake voice classification
- Real-time audio analysis
- Speaker verification
- Model confidence visualization
- Cloud deployment
- REST API integration
- Performance optimization

---

## Contributors

- **Ravuri Dharma Teja** *(Team Leader)*
- Project Team Members

---

## License

This project is developed for educational and internship purposes.

---

## Acknowledgements

- FastAPI
- React
- Vite
- Librosa
- PyTorch
- NumPy
- Matplotlib

---

⭐ If you found this project useful, consider giving it a star on GitHub.