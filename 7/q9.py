import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

e = conv.unmicro(6.12)

di = 7.3

# voltage from a loop assuming an ohmic circuit is 3/4 that of the battery but in the opposite direction
e_loop = e * 2 / 3
A = conv.cm2_to_m2(7.3)

print(e_loop / A)
