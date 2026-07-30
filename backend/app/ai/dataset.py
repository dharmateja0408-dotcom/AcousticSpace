import pandas as pd
from app.config import PROTOCOL_DIR


def load_train_protocol():

    protocol_file = (
        PROTOCOL_DIR /
        "ASVspoof2019.LA.cm.train.trn.txt"
    )

    df = pd.read_csv(
        protocol_file,
        sep=r"\s+",
        header=None,
        names=[
            "speaker",
            "filename",
            "unused",
            "attack",
            "label"
        ],
        engine="python"
    )

    return df