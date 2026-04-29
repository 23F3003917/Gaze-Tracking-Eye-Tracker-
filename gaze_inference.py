import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from pathlib import Path

# ---------------- CONFIG ----------------
OPENFACE_CSV = "../../OpenFace/build/gaze_output/webcam.csv"
MODEL_PATH = "../models/saved_models/gaze_cnn.h5"
OUTPUT_CSV = "../../OpenFace/build/gaze_output/webcam.csv"

FEATURES = [
    "gaze_0_x", "gaze_0_y", "gaze_0_z",
    "gaze_1_x", "gaze_1_y", "gaze_1_z",
    "pose_Tx", "pose_Ty", "pose_Tz",
    "pose_Rx", "pose_Ry", "pose_Rz"
]
# ----------------------------------------

print("📥 Loading OpenFace CSV...")
df = pd.read_csv(OPENFACE_CSV)

# 🔧 FIX COLUMN ISSUE (VERY IMPORTANT)
df.columns = df.columns.str.strip()

# Drop rows with missing gaze/pose
df = df.dropna(subset=FEATURES)

X = df[FEATURES].values.astype(np.float32)

print("🧠 Loading gaze CNN model...")
model = load_model(MODEL_PATH)

print("🎯 Predicting gaze...")
predictions = model.predict(X)

df["screen_x"] = predictions[:, 0]
df["screen_y"] = predictions[:, 1]

df.to_csv(OUTPUT_CSV, index=False)

print(f"✅ Gaze predictions saved to: {OUTPUT_CSV}")
