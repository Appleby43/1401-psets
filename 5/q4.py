import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

A = 2.4 * 10 **-6
L = 3.2
I = 2.8

# resistivity of copper from textbook
rho = 1.69 * 10 ** -8
j = I / A

E = rho * j
print(E)

R = rho * (L / A)
P = I ** 2 * R
print(conv.mins_to_sec(25) * P)
