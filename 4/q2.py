import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

print(180)

L = conv.cm_to_m(11.7)
charge = conv.unfemto(47.7)
density = charge / L
d = conv.cm_to_m(6.53)

E = density * L / (4 * math.pi * const.e_0 * d * (d + L))

print(-E)
