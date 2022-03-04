import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

print("equal")

# potential inside a sphere = kq / r

sphere_2_scale = 4 # how much larger is the radius of sphere 2 to sphere 1

## because q1 / q2 = 1 / scale
total_q_proportions = sphere_2_scale + 1

print(1 / total_q_proportions)
print(sphere_2_scale / total_q_proportions)

print(sphere_2_scale)
