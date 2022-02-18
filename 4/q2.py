import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

print(180)

L = conv.cm_to_m(14.2)
charge = conv.unfemto(77.3)
density = charge / L
d = conv.cm_to_m(9.63)

E = density * L / (4 * math.pi * const.e_0 * d * (d + L))

print(E)
