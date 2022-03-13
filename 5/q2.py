import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

resistence = 6.9

length_change = 4
area_change = 1 / length_change

print(resistence * (length_change / area_change))

