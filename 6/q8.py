import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

I_w1 = 6.3
d1 = conv.cm_to_m(0.75)
d2 = conv.cm_to_m(1.5)

B_w1 = const.u_0 * I_w1 / (2 * math.pi * (d1 + d2)) 

I_w2 = 2 * math.pi * d2 * B_w1 / (const.u_0)
print(I_w2)
