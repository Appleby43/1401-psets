import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

p = 1.69 * 10 ** -8
L = conv.cm_to_m(71.7)
d = conv.mm_to_m(0.782)

A_wire = math.pi * (d / 2) ** 2

R = p * L / A_wire

radius = L / (2 * math.pi)

A_loop = math.pi * radius ** 2

dB_dT = conv.unmilli(11)

E = dB_dT * A_loop

i = E / R

power = i ** 2 * R
print(power)
