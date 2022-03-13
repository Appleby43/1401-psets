import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv
import resistor

#solve V = E * (1 - e^(-t / RC)) for R
t = 1 / 3
E = 91.6
breakdown_v = 70.2
C = conv.unmilli(.104)

R = t / (C * math.log(E / (E - breakdown_v)))

print(R)
