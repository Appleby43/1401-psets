import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

i1 = 5.5
i2 = 2.5

print(const.u_0 * (i2 - i1))
# keep track of the direction of each loop that each current passes through
print(const.u_0 * (-i1 - i1 - i2))
