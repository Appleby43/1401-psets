import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

def arc_field(i, theta, r):
    return const.u_0 * i * math.radians(theta) / (4 * math.pi * r)

I1 = 0.49
I2 = 2 * I1

r1 = conv.cm_to_m(5.4)
r2 = conv.cm_to_m(4.7)

B1 = arc_field(I1, 180, r1)
B2 = arc_field(I2, 120, r2) 

print(conv.micro(B2 - B1))
print(conv.micro(B1 + B2))
