import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from feature_dataset import FeatureDataset
from model import CNNClassifier

# -----------------------------
# Configuration
# -----------------------------

FEATURE_DIR = "dataset/processed/features"
LABEL_DIR = "dataset/processed/labels"

BATCH_SIZE = 32
EPOCHS = 10
LEARNING_RATE = 0.001

# -----------------------------
# Dataset & DataLoader
# -----------------------------

dataset = FeatureDataset(FEATURE_DIR, LABEL_DIR)

train_loader = DataLoader(
    dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

# -----------------------------
# Model
# -----------------------------

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = CNNClassifier().to(device)

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)

# -----------------------------
# Training Loop
# -----------------------------

for epoch in range(EPOCHS):

    model.train()

    running_loss = 0.0

    for features, labels in train_loader:

        features = features.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(features)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    print(
        f"Epoch {epoch+1}/{EPOCHS} | "
        f"Loss: {running_loss/len(train_loader):.4f}"
    )

# -----------------------------
# Save Model
# -----------------------------

torch.save(
    model.state_dict(),
    "models/baseline_cnn.pth"
)

print("\nModel saved successfully!")