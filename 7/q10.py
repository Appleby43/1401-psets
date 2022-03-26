import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

F = 53.3
B = 0.495
E_0 = 239

print(E_0 / (F * B * 2 * math.pi))
