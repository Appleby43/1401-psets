import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv
import resistor

C = conv.unmilli(1.32)
U = 0.761
t = 694
R = 1.8 * 10**6 

q0 = math.sqrt(2 * C * U)
print(q0)

I = q0 / (R * C)

print(I)

V = (q0 / C) *  math.exp(-t / (R * C))
print(V)
print(V)

P = V ** 2 / R

print(P)
