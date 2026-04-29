import pandas as pd

df = pd.read_csv("gaze_output/webcam.csv")

print(df[[
    "frame",
    "gaze_angle_x",
    "gaze_angle_y",
    "pose_Rx",
    "pose_Ry"
]].head())
