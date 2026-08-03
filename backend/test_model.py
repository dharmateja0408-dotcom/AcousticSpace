import torch
from model import CNNClassifier

model = CNNClassifier()

x = torch.randn(8, 1, 40, 300)

output = model(x)

print("Output shape:", output.shape)