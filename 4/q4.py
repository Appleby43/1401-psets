import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

a = conv.mm_to_m(37.8)
b = conv.mm_to_m(39.1)

C = 4 * math.pi * const.e_0 / ((1 / a) - (1 / b))
print(conv.pico(C))

separation = b - a

# rearrange C = e_0 * A / d
A = C * separation / const.e_0
print(conv.m2_to_cm2(A))
