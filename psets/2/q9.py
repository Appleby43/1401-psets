import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

area = 1.4
E = 77
E_per_plate = E / 2

sigma = 2 * const.e_0 * E_per_plate

print(sigma * area)
