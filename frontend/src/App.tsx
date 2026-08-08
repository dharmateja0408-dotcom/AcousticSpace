import { useState } from "react";
import axios from "axios";
import "./App.css";

import AudioUpload from "./components/AudioUpload";
import Waveform from "./components/Waveform";

interface PredictionResponse {
  status: string;
  filename: string;
  prediction: string;
  confidence: number;
  risk: string;
  recommendation: string;
  duration: number;
  sample_rate: number;
  analysis_time: number;
  report: string;
}

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [prediction, setPrediction] =
    useState<PredictionResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileSelect = async (file: File) => {
    setSelectedFile(file);
    setPrediction(null);
    setError("");

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/upload/",
        formData
      );

      setPrediction(response.data);
    } catch (err) {
      console.error(err);
      setError(
        "Unable to analyze this audio. Please make sure the backend is running."
      );
    } finally {
      setLoading(false);
    }
  };

  const isSpoof = prediction?.prediction?.toLowerCase() === "spoof";

  return (
    <div className="app">
      <header className="navbar">
        <div className="brand">
          <div className="brand-icon">◉</div>
          <div>
            <h1>AcousticSpace</h1>
            <span>AI Audio Intelligence</span>
          </div>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          System Online
        </div>
      </header>

      <main className="main">
        <section className="hero">
          <div className="hero-badge">
            <span>✦</span> AI-POWERED AUDIO ANALYSIS
          </div>

          <h2>
            Detect synthetic speech
            <br />
            <span>with confidence.</span>
          </h2>

          <p>
            Upload an audio recording and let AcousticSpace analyze its
            acoustic characteristics for signs of synthetic or manipulated
            speech.
          </p>
        </section>

        <section className="upload-card">
          <AudioUpload onFileSelect={handleFileSelect} />

          {selectedFile && (
            <div className="selected-file">
              <div className="file-icon">♫</div>

              <div className="file-info">
                <strong>{selectedFile.name}</strong>
                <span>
                  {(selectedFile.size / (1024 * 1024)).toFixed(2)} MB
                </span>
              </div>

              {!loading && <span className="file-ready">Ready</span>}
            </div>
          )}

          {selectedFile && <Waveform file={selectedFile} />}

          {loading && (
            <div className="analyzing">
              <div className="spinner"></div>

              <div>
                <strong>Analyzing audio...</strong>
                <span>
                  Extracting acoustic features and running AI detection
                </span>
              </div>
            </div>
          )}

          {error && <div className="error-box">⚠ {error}</div>}
        </section>

        {prediction && !loading && (
          <section className="results">
            <div className="section-heading">
              <div>
                <span className="eyebrow">ANALYSIS COMPLETE</span>
                <h3>Detection Results</h3>
              </div>

              <span className="completed">✓ Completed</span>
            </div>

            <div className="result-grid">
              <div
                className={`prediction-card ${
                  isSpoof ? "spoof" : "bonafide"
                }`}
              >
                <span className="card-label">DETECTION</span>

                <div className="prediction-icon">
                  {isSpoof ? "!" : "✓"}
                </div>

                <h4>{prediction.prediction}</h4>

                <p>
                  {isSpoof
                    ? "Potential synthetic or manipulated speech detected."
                    : "No strong indicators of synthetic speech detected."}
                </p>
              </div>

              <div className="confidence-card">
                <span className="card-label">CONFIDENCE</span>

                <div className="confidence-value">
                  {prediction.confidence}
                  <small>%</small>
                </div>

                <div className="confidence-bar">
                  <div
                    style={{
                      width: `${prediction.confidence}%`,
                    }}
                  ></div>
                </div>

                <span className="muted">
                  Model prediction confidence
                </span>
              </div>

              <div className="risk-card">
                <span className="card-label">RISK LEVEL</span>

                <div className={`risk-badge ${prediction.risk.toLowerCase()}`}>
                  {prediction.risk}
                </div>

                <p>
                  {prediction.risk === "High"
                    ? "Manual verification is recommended."
                    : "No high-risk indicators detected."}
                </p>
              </div>
            </div>

            <div className="stats-grid">
              <div className="stat-card">
                <span>Duration</span>
                <strong>{prediction.duration}s</strong>
              </div>

              <div className="stat-card">
                <span>Sample Rate</span>
                <strong>{prediction.sample_rate} Hz</strong>
              </div>

              <div className="stat-card">
                <span>Analysis Time</span>
                <strong>{prediction.analysis_time}s</strong>
              </div>

              <div className="stat-card">
                <span>File</span>
                <strong title={prediction.filename}>
                  {prediction.filename.length > 18
                    ? `${prediction.filename.substring(0, 18)}...`
                    : prediction.filename}
                </strong>
              </div>
            </div>

            <div className="recommendation">
              <div className="recommendation-icon">✦</div>

              <div>
                <span className="card-label">AI RECOMMENDATION</span>
                <p>{prediction.recommendation}</p>
              </div>
            </div>

            <div className="report-section">
              <div>
                <h4>Detailed analysis report</h4>
                <p>
                  Download the complete AcousticSpace analysis as a PDF.
                </p>
              </div>

              <a
                className="download-button"
                href="http://127.0.0.1:8000/upload/report"
                target="_blank"
                rel="noopener noreferrer"
              >
                ↓ Download PDF
              </a>
            </div>
          </section>
        )}

        {!prediction && !loading && (
          <section className="features">
            <div className="feature">
              <span>01</span>
              <div>
                <strong>Upload</strong>
                <p>Select any supported audio recording.</p>
              </div>
            </div>

            <div className="feature">
              <span>02</span>
              <div>
                <strong>Analyze</strong>
                <p>Our AI extracts acoustic characteristics.</p>
              </div>
            </div>

            <div className="feature">
              <span>03</span>
              <div>
                <strong>Understand</strong>
                <p>Get prediction, confidence and risk insights.</p>
              </div>
            </div>
          </section>
        )}
      </main>

      <footer>
        <span>AcousticSpace v1.0</span>
        <span>AI Audio Spoof Detection</span>
      </footer>
    </div>
  );
}

export default App;
