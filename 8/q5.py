import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

dB_dt =  conv.unmilli(7.23)

r1 = conv.cm_to_m(6.36)
# from integral e * ds = dFlux_dt
E = (r1 / 2) * dB_dt

print(E)

r2 = conv.cm_to_m(10.7) 
d_sol = conv.cm_to_m(16.1)
r_sol = d_sol / 2
a_sol = math.pi * r_sol ** 2
E2 = a_sol * dB_dt / (2 * math.pi * r2)
print(E2)
