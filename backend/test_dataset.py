from dataset_loader import ASVspoofDataset

dataset = ASVspoofDataset(
    protocol_file="dataset/LA/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt",
    audio_dir="dataset/LA/ASVspoof2019_LA_train/flac"
)

print("Number of samples:", len(dataset))