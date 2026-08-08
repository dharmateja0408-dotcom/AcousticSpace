import React, { useRef, useState } from "react";

interface AudioUploadProps {
  onFileSelect: (file: File) => void;
}

const AudioUpload: React.FC<AudioUploadProps> = ({ onFileSelect }) => {
  const inputRef = useRef<HTMLInputElement | null>(null);
  const [dragging, setDragging] = useState(false);

  const handleFile = (file?: File) => {
    if (!file) return;

    if (!file.type.startsWith("audio/")) {
      alert("Please select an audio file.");
      return;
    }

    onFileSelect(file);
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    handleFile(event.target.files?.[0]);
  };

  return (
    <div
      className={`upload-zone ${dragging ? "dragging" : ""}`}
      onClick={() => inputRef.current?.click()}
      onDragOver={(event) => {
        event.preventDefault();
        setDragging(true);
      }}
      onDragLeave={() => setDragging(false)}
      onDrop={(event) => {
        event.preventDefault();
        setDragging(false);
        handleFile(event.dataTransfer.files?.[0]);
      }}
    >
      <input
        ref={inputRef}
        type="file"
        accept="audio/*"
        onChange={handleChange}
        hidden
      />

      <div className="upload-icon">↑</div>

      <h3>Drop your audio here</h3>

      <p>
        or <span>browse files</span>
      </p>

      <small>
        WAV, MP3, FLAC and other supported audio formats
      </small>
    </div>
  );
};

export default AudioUpload;
