import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

R1 = conv.mm_to_m(1.6)
R2 = 12.6 * R1
L = 13.7

Q1 = 3.44 * 10**-12
Q2 = -2.18 * Q1

E = (Q1 + Q2) / (2 * math.pi * const.e_0 * 2.04 * R2 * L)
print(E)

E2 = (Q1) / (2 * math.pi * const.e_0 * 5.05 * R1 * L)
print(E2)

print(-Q1)

print(Q2 + Q1)
