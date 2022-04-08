import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

v = 7.73
b = 0.422

# Area = v^2t^2 by pythag
t = 3.17
area = (v ** 2) * (t ** 2)
print(area * b)

da_dt = 2 * t * v ** 2

dFlux_dt = da_dt * b

print(dFlux_dt)

print(1)
