import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

l = conv.cm_to_m(38.5)
L = np.array([l, 0, 0])
B = np.array([0, 0.000410, 0.0110])
I = 0.58

F = I * (np.cross(L, B))

print(F[0])
print(F[1])
print(F[2])
