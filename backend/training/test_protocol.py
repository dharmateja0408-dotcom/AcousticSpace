from app.ai.dataset import load_train_protocol

df = load_train_protocol()

print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nLabel Counts:")
print(df["label"].value_counts())