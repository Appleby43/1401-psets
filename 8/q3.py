import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

N = 120

w = conv.cm_to_m(64.1)
h = conv.cm_to_m(24.1)

A = w * h 

B = 3.45

rot = 1290 / 60

print(N * 2 * math.pi * rot * B * A)
