import React, { useEffect, useRef } from "react";
import WaveSurfer from "wavesurfer.js";

interface WaveformProps {
  file: File | null;
}

const Waveform: React.FC<WaveformProps> = ({ file }) => {
  const waveformRef = useRef<HTMLDivElement>(null);
  const wavesurfer = useRef<WaveSurfer | null>(null);

  useEffect(() => {
    if (!waveformRef.current) return;

    if (wavesurfer.current) {
      wavesurfer.current.destroy();
    }

    wavesurfer.current = WaveSurfer.create({
      container: waveformRef.current,
      waveColor: "#4F46E5",
      progressColor: "#EF4444",
      height: 120,
    });

    if (file) {
      const url = URL.createObjectURL(file);
      wavesurfer.current.load(url);
    }

    return () => {
      wavesurfer.current?.destroy();
    };
  }, [file]);

  return <div ref={waveformRef}></div>;
};

export default Waveform;