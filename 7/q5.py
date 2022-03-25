import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

# integrate J dA from 0 to r
# note that dA / dr = 2pi * r, thus dA = 2pi * r dr

J_0 = 300
a = conv.mm_to_m(3.2)

factor = 2 * math.pi * J_0 / (3 * a) 
def i(r):
    return factor * r ** 3

def perim(r):
    return math.pi * 2 * r

print(0)
r2 = conv.mm_to_m(2.1)

B2 = const.u_0 * i(r2) / perim(r2)
print(B2)

B3 = const.u_0 * i(a) / perim(a)
print(B3)
