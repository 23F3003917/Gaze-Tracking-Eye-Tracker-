import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "gaze_predictions.csv"

df = pd.read_csv(CSV_PATH)

plt.figure(figsize=(7, 7))
plt.scatter(df["gaze_x"], df["gaze_y"], s=3, alpha=0.6)
plt.gca().invert_yaxis()
plt.title("Predicted Gaze Points")
plt.xlabel("Screen X")
plt.ylabel("Screen Y")
plt.grid(True)
plt.show()
