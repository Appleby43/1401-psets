import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

di_dt = conv.unkilo(30)
E = 24
L = E / di_dt

print(L)
