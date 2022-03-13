import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

I = conv.unmilli(.94)
E1 = 2.3
E2 = 4.0
R12 = 2.4

# by voltage law, E2 = E1 - IR1 - IR2 - IR = 0
R = (E2 - E1 - (2 * R12 * I)) / I    

print(R)

P = I ** 2 * R
print(P)
