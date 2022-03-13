import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

R = conv.mm_to_m(2.06)
constant_factor = 3.15 * 10 ** 8

inner_r_factor = 0.914

# integrate J Da where Da = 2 * pi * r * dr

coeff = (constant_factor * math.pi ) / 2

integral_result = R ** 4 - (inner_r_factor * R) ** 4

print(conv.milli(coeff * integral_result))
