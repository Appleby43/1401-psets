import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

E1 = 5.16
E2 = 10.3

R1 = 107
R2 = 188
R3 = 279

#term_1 = -1 * (E1 / R3)
#term_2 = (R2 * E1 - R1 * R2 * I3) / (R3 * (R2 + R1))
#term_3 = E2 / R3

#fuck this im using a systems solver
