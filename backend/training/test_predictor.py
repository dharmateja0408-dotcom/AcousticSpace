




from app.ai.predictor import predict_audio
from app.config import TRAIN_AUDIO_DIR

audio = list(TRAIN_AUDIO_DIR.glob("*.flac"))[0]

print(audio)

result = predict_audio(audio)

print(result)