import React, { useEffect, useRef } from "react";
import WaveSurfer from "wavesurfer.js";

interface WaveformProps {
  file: File | null;
}

const Waveform: React.FC<WaveformProps> = ({ file }) => {
  const waveformRef = useRef<HTMLDivElement | null>(null);
  const wavesurfer = useRef<WaveSurfer | null>(null);

  useEffect(() => {
    if (!waveformRef.current || !file) return;

    wavesurfer.current?.destroy();

    const url = URL.createObjectURL(file);

    wavesurfer.current = WaveSurfer.create({
      container: waveformRef.current,
      waveColor: "#465574",
      progressColor: "#7086ff",
      cursorColor: "#9aa8ff",
      height: 90,
      barWidth: 2,
      barGap: 2,
      barRadius: 3,
    });

    wavesurfer.current.load(url);

    return () => {
      wavesurfer.current?.destroy();
      URL.revokeObjectURL(url);
    };
  }, [file]);

  return (
    <div className="waveform-wrapper">
      <div className="waveform-label">
        <span>AUDIO WAVEFORM</span>
        <span>Preview</span>
      </div>

      <div ref={waveformRef} />
    </div>
  );
};

export default Waveform;
