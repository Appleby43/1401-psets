import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

B = 0.569
p = conv.unmicro(5.22)
F = 1.78 * 10 ** -15

T = 2 * math.pi * const.electron_mass / (const.elementary_charge * B)
v_par = p / T

# since F = vperp * q * B
v_perp = F / (const.electron_charge * B)
speed = math.hypot(v_par, v_perp)

print(conv.kilo(speed))

