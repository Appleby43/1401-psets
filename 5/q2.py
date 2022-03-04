import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

resistence = 7.1

length_change = 3
area_change = 1 / length_change

print(resistence * (length_change / area_change))

