import os
import numpy as np
import torch
from torch.utils.data import Dataset


class FeatureDataset(Dataset):

    def __init__(self, feature_dir, label_dir):

        self.feature_dir = feature_dir
        self.label_dir = label_dir

        self.files = sorted(os.listdir(feature_dir))

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):

        file = self.files[idx]

        feature = np.load(
            os.path.join(self.feature_dir, file)
        )

        label = np.load(
            os.path.join(self.label_dir, file)
        )

        feature = torch.tensor(
            feature,
            dtype=torch.float32
        )

        feature = feature.unsqueeze(0)

        label = torch.tensor(
            label,
            dtype=torch.long
        )

        return feature, label