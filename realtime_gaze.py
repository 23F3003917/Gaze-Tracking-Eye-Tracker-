import subprocess
import pandas as pd
import time
import cv2
import numpy as np
import os

OPENFACE_BIN = "/Users/anirudhsinghtomar/Desktop/GazeTracking/OpenFace/build/bin/FeatureExtraction"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Start OpenFace (CSV MODE)
proc = subprocess.Popen([
    OPENFACE_BIN,
    "-device", "0",
    "-gaze",
    "-pose",
    "-out_dir", OUTPUT_DIR,
    "-of", "live"
])

CSV_PATH = f"{OUTPUT_DIR}/live.csv"

print("👁️ OpenFace started — waiting for gaze data...")

# Screen size (adjust if needed)
SCREEN_W, SCREEN_H = 1440, 900

last_point = None
fix_start = None
FIX_TIME = 1.0

while True:
    if not os.path.exists(CSV_PATH):
        time.sleep(0.1)
        continue

    try:
        df = pd.read_csv(CSV_PATH)

        if len(df) < 2:
            continue

        row = df.iloc[-1]

        gaze_x = row["gaze_0_x"]
        gaze_y = row["gaze_0_y"]

        # Normalize gaze → screen
        screen_x = int((gaze_x + 1) * 0.5 * SCREEN_W)
        screen_y = int((1 - gaze_y) * 0.5 * SCREEN_H)

        # Fixation detection
        now = time.time()
        if last_point:
            dist = np.linalg.norm(np.array(last_point) - np.array((screen_x, screen_y)))
            if dist < 30:
                if fix_start and now - fix_start > FIX_TIME:
                    print(f"📌 FIXATION at ({screen_x}, {screen_y})")
                    fix_start = None  # prevent spamming

            else:
                fix_start = now
        else:
            fix_start = now

        last_point = (screen_x, screen_y)

        # Visualize
        canvas = np.zeros((SCREEN_H, SCREEN_W, 3), dtype=np.uint8)
        cv2.circle(canvas, (screen_x, screen_y), 12, (0, 255, 0), -1)
        cv2.imshow("Real-Time Gaze", canvas)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    except Exception:
        pass

proc.terminate()
cv2.destroyAllWindows()
