import os

import librosa
import numpy as np
import torch
from torch.utils.data import Dataset
class ASVspoofDataset(Dataset):

    def __init__(self, protocol_file, audio_dir):
        self.audio_dir = audio_dir
        self.samples = []

        with open(protocol_file, "r") as f:
            for line in f:
                parts = line.strip().split()

                file_id = parts[1]
                label = parts[-1]

                self.samples.append((file_id, label))
    def __len__(self):
        return len(self.samples)