from feature_dataset import FeatureDataset

dataset = FeatureDataset(
    "dataset/processed/features",
    "dataset/processed/labels"
)

print("Dataset Size:", len(dataset))

feature, label = dataset[0]

print("Feature Shape:", feature.shape)
print("Label:", label)