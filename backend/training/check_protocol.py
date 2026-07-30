




from pathlib import Path

protocol = Path(
    r"E:\AI_Datasets\ASVspoof2019\ASVspoof2019_LA_cm_protocols\ASVspoof2019.LA.cm.train.trn.txt"
)

with open(protocol, "r") as f:
    for i in range(5):
        print(f.readline())