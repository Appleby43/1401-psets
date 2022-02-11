import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

c = conv.unpico(11.6)
L = conv.cm_to_m(19.9)
d = conv.cm_to_m(5.34)

v = const.k * c * (math.sqrt(d ** 2 + L ** 2) - d)

y_comp = const.k * c * (1 - ( d / math.sqrt(d ** 2 + L ** 2)))

print(v)
print(y_comp)
