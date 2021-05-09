import numpy as np

from PIL import Image

import math

from tqdm import tqdm as ProgressBar

# * Constant

IMG_HEIGHT = 1080
IMG_WIDTH = 1080

S_POSITION_H = 540
S_POSITION_W = 540

WAVE_LENGTH = 10
WAVE_SPEED = 3
WAVE_AMPITUDE = 255
STARTING_PHASE = 0

PI = math.pi

picture = np.zeros((IMG_WIDTH, IMG_HEIGHT), np.uint8)


def Wave(d, t):
    k = 2 * PI / WAVE_LENGTH
    omega = 2 * PI * WAVE_SPEED / WAVE_LENGTH
    return WAVE_AMPITUDE * math.sin(k * d - omega * t + STARTING_PHASE)


def distance(x, y):
    return math.sqrt((x - S_POSITION_H) ** 2 + (y - S_POSITION_W) ** 2)


for x in ProgressBar(range(IMG_WIDTH)):
    for y in range(IMG_HEIGHT):
        picture[x][y] = Wave(distance(x, y), 0)

PictureObj = Image.fromarray(picture)

PictureObj.save("./generated/FirstWave.png")
