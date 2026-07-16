import "./App.css";

function App() {
  return (
    <div className="container">
      <h1>🎤 AcousticSpace Dashboard</h1>

      <div className="card">
        <h2>Upload Audio</h2>

        <input type="file" accept=".wav,.mp3,.flac" />

        <p>No file selected</p>
      </div>

      <div className="card">
        <h2>Analysis Results</h2>

        <p><strong>Sample Rate:</strong> --</p>

        <p><strong>Duration:</strong> --</p>

        <p><strong>Spectrogram:</strong> Waiting...</p>

        <p><strong>MFCC:</strong> Waiting...</p>
      </div>
    </div>
  );
}

export default App;
