import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

# B * A = u0 * i

i = 46.3
a = conv.cm_to_m(2.98)

def area(r):
    return math.pi * r ** 2

def perim(r):
    return 2 * math.pi * r

print(0)

r2 = conv.cm_to_m(1.5)
i2 = i * (area(r2) / area(a))

B2 = const.u_0 * i2 / perim(r2) 
print(B2)

B3 = const.u_0 * i / perim(a) 
print(B3)

r4 = conv.cm_to_m(3.92)
B4 = const.u_0 * i / perim(r4) 

print(B4)
