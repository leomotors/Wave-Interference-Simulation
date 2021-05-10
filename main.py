from tools.Wave_Class import Wave

import numpy as np
from PIL import Image
from tqdm import tqdm as ProgressBar
import math

FRAMES = int(input("Frames Count: "))

SPREADING = int(input("[Wave Config] Spreading: "))

TICK_RATE = 0.1

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

print("\nImage Processing...")
images = []
for frame in ProgressBar(range(FRAMES)):
    Picture_Array = np.zeros((IMG_WIDTH, IMG_HEIGHT), np.uint8)
    for pixel in ProgressBar(range(IMG_WIDTH*IMG_HEIGHT), leave=False):
        x = math.floor(pixel/IMG_HEIGHT)
        y = pixel % IMG_HEIGHT
        thisAmplitude = 127
        for wind in range(WAVE_COUNT):
            subWaveAmp = Wave_F1[wind](Wave_F2[wind](x, y), TICK_RATE * frame)
            thisAmplitude += subWaveAmp
        Picture_Array[x][y] = thisAmplitude
    Image_Obj = Image.fromarray(Picture_Array)
    images.append(Image_Obj)

print("\nImage Processing done. Saving files...")
images[0].save("./generated/{}.gif".format(fname),
               save_all=True, append_images=images[1:])
print("Saving DONE!")
