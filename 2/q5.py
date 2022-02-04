import math

import sys
sys.path.append('../')

import constants as const

w = 2.5
l = 2.2
h = 3.9

volume = w * l * h

area_wh = w * h
area_wl = w * l
area_hl = h * l

E = 736

#flux = E * A cos theta
flux = E * 2 * (area_hl + area_wl + area_wh)

q = flux * const.e_0
rho = q / volume
excess_charges = q / const.elementary_charge
excess_charges_per_meter = excess_charges / volume
print(rho)
print(excess_charges_per_meter)
print("units are 1/m^3 for b)")
