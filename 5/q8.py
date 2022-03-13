import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv
import resistor

RV = 360
RA = 4.03

R0 = 100
R = 118
E = 12

#find equivalent resistence of full circuit

parallel_bit = resistor.parallel([R, RV])
R_eq = resistor.series([parallel_bit, RA, R0])

i = E / R_eq
print(conv.milli(i))

paral_V = i * parallel_bit

print(paral_V)

print(paral_V / i)
