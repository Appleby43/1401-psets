import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

axis_scale = 4 * 10**5

flux_1 = axis_scale * (2 / 5) 
flux_2 = axis_scale * (-4 / 5)
flux_3 = axis_scale * (6 / 5)

def flux_to_charge(flux):
    return flux * const.e_0

print("units are in microculombs")
center_charge = flux_to_charge(flux_1)
print(conv.C_to_uC(center_charge))

charge_a = flux_to_charge(flux_2) - center_charge
print(conv.C_to_uC(charge_a))

charge_b = flux_to_charge(flux_3) - center_charge - charge_a
print(conv.C_to_uC(charge_b))
