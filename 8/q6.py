import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

radius = conv.cm_to_m(9.46)
N = 27

B = conv.unmilli(2.87)

A = math.pi * radius ** 2
flux = B * A
print(flux * N)

i = 3.28

L = flux * N / i
print(L)
