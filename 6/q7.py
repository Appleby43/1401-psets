import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

print(90)
print(1)

circumference = conv.cm_to_m(20.1)
I = conv.unmilli(5)
B = conv.unmilli(4.63)

# circumference = 2 pi r
r = circumference / (2 * math.pi)
A = math.pi * (r ** 2)

T = I * A * B
print(T)
