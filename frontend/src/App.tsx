import { useState } from "react";
import axios from "axios";
import "./App.css";

import AudioUpload from "./components/AudioUpload";
import Waveform from "./components/Waveform";

interface PredictionResponse {
  filename: string;
  prediction: string;
  confidence: number;
}

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [prediction, setPrediction] = useState<PredictionResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleFileSelect = async (file: File) => {
    setSelectedFile(file);
    setPrediction(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/predict",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setPrediction(response.data);
    } catch (error) {
      console.error(error);
      alert("Prediction failed!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "900px",
        margin: "40px auto",
        padding: "20px",
        fontFamily: "Arial",
      }}
    >
      <h1>🎤 AcousticSpace</h1>

      <h2>Audio Spoof Detection</h2>

      <AudioUpload onFileSelect={handleFileSelect} />

      {selectedFile && (
        <>
          <p>
            <strong>Selected:</strong> {selectedFile.name}
          </p>

          <Waveform file={selectedFile} />
        </>
      )}

      {loading && (
        <h3>Predicting...</h3>
      )}

      {prediction && (
        <div
          style={{
            marginTop: "20px",
            padding: "15px",
            border: "1px solid #ddd",
            borderRadius: "10px",
          }}
        >
          <h2>Prediction Result</h2>

          <p>
            <strong>Prediction:</strong> {prediction.prediction}
          </p>

          <p>
            <strong>Confidence:</strong> {prediction.confidence}%
          </p>
        </div>
      )}
    </div>
  );
}

export default App;