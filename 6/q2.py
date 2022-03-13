import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

B = conv.unmilli(3.4)
v = 2990
E = 3.05

Bvec = np.array([-B, 0, 0])
Vvec = np.array([0, v, 0])

F_m = np.cross(Vvec, Bvec)
F_m = F_m * const.elementary_charge

F_mz = F_m[2]
F_ez = E * const.elementary_charge 
print(F_mz + F_ez)
print(F_mz - F_ez)

Evec = np.array([E, 0, 0 ]) * const.elementary_charge

mag = np.linalg.norm(Evec + F_m)
print(mag)
