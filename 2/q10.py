import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

R = conv.cm_to_m(6.4)
p_coeff = conv.unpico(15.7)

# integrate density * dV where dV = 4 * pi * r^2
def integrated_charge(r):
    return (math.pi * p_coeff * r**4) / R

# defininite integral from r = 0 to r = R
charge = integrated_charge(R) - integrated_charge(0)
print(conv.femto(charge))

print(0)

def area_of_sphere(r):
    return 4 * math.pi * r ** 2

charge2 = integrated_charge(R / 3) - integrated_charge(0)

E2 = charge2 / (const.e_0 * area_of_sphere(R / 3))

print(conv.milli(E2))

E3 = charge / (const.e_0 * area_of_sphere(R))
print(conv.milli(E3))
