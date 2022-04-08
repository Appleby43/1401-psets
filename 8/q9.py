import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

E = 14
R = 6.3
L = 6.5
t = 3
tau = L / R

# integrate P = i(t) * V with respect to time
coeff = E * E / R
eterm = math.exp(-t / tau)

P = coeff * (t +  (tau) * (eterm - 1))
print(P)

i = (E / R) * (1 - math.exp(-t / tau))
U = (1 / 2) * L * i ** 2
print(U)
print(P - U)
