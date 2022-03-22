import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

i = conv.unmilli(3.72)

R = conv.cm_to_m(1.62)

B_wire = const.u_0 * i / (2 * math.pi * R)

B_loop = const.u_0 * i / (2 * R)

print(0)
print(0)
print(B_wire + B_loop)

print(B_loop)
print(0)
print(B_wire)
