import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

D1 = 5
D2 = 3.5

n = 8.1 * 10 ** 28

A1 = math.pi *  (D1 / 2) ** 2
A2 = math.pi *  (D2 / 2) ** 2

# find the resistence across the sampled peice of wire
dV = conv.unmicro(13)
L = 2.1

# selected resistivity from textbook (copper)
rho = 1.69 * 10 ** -8

R = rho * (L / A2)
I = dV / R

# current conservation means that J2 * A2 = J1 * A1 = I
J1 = I / A1 
# print(J1)

v = J1 / (n * const.elementary_charge)
print(v)
