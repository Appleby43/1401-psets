import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

R = conv.cm_to_m(13.3)
L = conv.cm_to_m(18.4)

i = conv.unmilli(65)

# dB = u0 / 4pi * i ds sin theta / r^2

coeff = const.u_0 * i * R / (4 * math.pi)

#result of integration / antiderivative
def F(s):
    return s / ((R ** 2) * math.sqrt(R ** 2 + s ** 2))

improper_intgrl = coeff * (F(L / 2) - F(-L / 2))

print(improper_intgrl)

