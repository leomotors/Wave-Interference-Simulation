from tools.Wave_Class import Wave

import numpy as np
from PIL import Image
from tqdm import tqdm as ProgressBar

from utils.utils import *

print("Welcome to Wave Inteference Simulator!")
print("Here is where you can simulate waves inefficiency")
print()

FRAMES = int(input("Frames Count [-1 for auto]: "))

SPREADING = int(input("[Wave Config] Spreading [1-Yes, 0-No]: "))

TICK_RATE = 0.1
MIDDLE_AMPLITUDE = 127

IMG_HEIGHT, IMG_WIDTH = (int(k) for k in input("Height, Width: ").split())

WAVE_COUNT = int(input("Number of Waves: "))

List_Of_Wave = []

for wave in range(WAVE_COUNT):
    print("Wave #{} Property: ".format(wave+1))
    wpos = [int(k) for k in input("x, y Position: ").split()]
    cwp = [int(k)
           for k in input("Length, Speed, Amplitude, Starting Phase: ").split()]
    CurrWaveObj = Wave(cwp[0], cwp[1], cwp[2])
    CurrWaveObj.setPos(wpos[0], wpos[1])
    CurrWaveObj.setPhase(cwp[3])
    List_Of_Wave.append(CurrWaveObj)

fname = input("Please enter output file name: ")


print("Processing Wave...")
Wave_F1 = []
Wave_F2 = []
for wave in ProgressBar(List_Of_Wave):
    Wave_F1.append(wave.getWaveFunction(SPREADING))
    Wave_F2.append(wave.distanceFunction())

if FRAMES == -1:
   FRAMES = auto_frame_count(List_Of_Wave, IMG_HEIGHT, IMG_WIDTH, TICK_RATE)

# ! Inefficient part
print("\nImage Processing...")
images = []
for frame in ProgressBar(range(FRAMES)):
    Picture_Array = np.zeros((IMG_WIDTH, IMG_HEIGHT), np.uint8)
    for x in ProgressBar(range(IMG_WIDTH), leave=False):
        for y in ProgressBar(range(IMG_HEIGHT), leave=False):
            thisSum = 0
            for wind in range(WAVE_COUNT):
                subWaveAmp = Wave_F1[wind](
                    Wave_F2[wind](x, y), TICK_RATE * frame)
                thisSum += subWaveAmp
            Picture_Array[x][y] = MIDDLE_AMPLITUDE + thisSum
            
            if Picture_Array[x][y] >= 256:
                Picture_Array[x][y] = 255
            elif Picture_Array[x][y] < 0:
                Picture_Array[x][y] = 0
            
    Image_Obj = Image.fromarray(Picture_Array)
    images.append(Image_Obj)

print("\nImage Processing done. Saving files...")
if FRAMES > 1:
    images[0].save("./generated/{}.gif".format(fname),
                   save_all=True, append_images=images[1:])
else:
    images[0].save("./generated/{}.png".format(fname))
print("Saving DONE!")
