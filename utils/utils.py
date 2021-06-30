
# * Utils Function

from tools.Wave_Class import Wave

import math

def auto_frame_count(waves, h, w, tr):
    max_time = 0.0
    to_check = ((0, 0), (0, h), (0, w), (h, w))
    for wave in waves:
        temp_func = wave.distanceFunction()
        for p in to_check:
            temp_dist = temp_func(p[0], p[1])
            temp_time = temp_dist / wave.wavespeed
            if temp_time > max_time:
                max_time = temp_time
    
    return math.ceil((max_time / tr) * 1.1)
