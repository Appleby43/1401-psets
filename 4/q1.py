import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

radius = conv.cm_to_m(67.3)
distance = conv.cm_to_m(0.207)

sigma = conv.unfemto(5.40)

def potential_from_disc(d, r):
    const_factors = const.k * sigma * 2 * math.pi
    root = math.sqrt(d ** 2 + r ** 2) - d
    return const_factors * root

print(potential_from_disc(distance, radius) * 0.25)
