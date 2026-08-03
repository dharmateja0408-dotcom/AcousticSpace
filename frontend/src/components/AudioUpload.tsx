import React from "react";

interface AudioUploadProps {
  onFileSelect: (file: File) => void;
}

const AudioUpload: React.FC<AudioUploadProps> = ({ onFileSelect }) => {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files.length > 0) {
      onFileSelect(event.target.files[0]);
    }
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <input
        type="file"
        accept=".wav,.flac,.mp3"
        onChange={handleChange}
      />
    </div>
  );
};

export default AudioUpload;