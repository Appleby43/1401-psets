import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

N_sol = conv.cm_to_m(280)
I = 2.1

N_coil = 100
R = conv.cm_to_m(3.7 / 2)
A = math.pi * R ** 2

res = 5.2

B = const.u_0 * N_sol * I

flux = B * A

dT = conv.unmilli(37)

E_coil = -N_coil * (flux / dT)
print(E_coil)

I_coil = E_coil / res

print(I_coil)
