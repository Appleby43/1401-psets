import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

# B = uNI
# N = B/uI

#L = conv.cm_to_m(35)
D = conv.cm_to_m(9.7)
I = 0.41
R = conv.cm_to_m(9.7) / 2

A = math.pi * R ** 2

N = 230
print(N * I * A)
