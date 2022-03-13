import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

E1 = 2.2 
E23 = 5
R1 = 0.75
R2 = 1.5

# stol'd from textbook 
i = 2 * (E23 - E1) / (4 * R1 + R2)
print(i)

print(i / 2)
print(i / 2)

diff = E23 - (i / 2) * R2
print(diff)
