import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

d1 = conv.cm_to_m(2.5)
d2 = conv.cm_to_m(5.08)

I1 = conv.unmilli(4.28)
I2 = conv.unmilli(7.05)

d = math.hypot(d1, d2) 
theta = math.atan2(d1, d2)

F_per_L = const.u_0 * I1 * I2 / (2 * math.pi * d)
print(F_per_L * math.cos(theta))
