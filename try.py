import numpy as np

SCREEN_W = 1920
SCREEN_H = 1080

def gaze_to_screen(gx, gy):
    x = (gx + 0.5) * SCREEN_W
    y = (gy + 0.5) * SCREEN_H
    return int(x), int(y)
