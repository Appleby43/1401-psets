import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

E1 = 2.4
E23 = 3.6
R1 = 1.5
R2 = 3

# stol'd from textbook 
i = 2 * (E23 - E1) / (4 * R1 + R2)
print(i)

print(i / 2)
print(i / 2)

diff = E23 - (i / 2) * R2
print(diff)
