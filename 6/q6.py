import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

N = 27
x_dist = conv.cm_to_m(5.5)
y_len = conv.cm_to_m(13) 
I = 0.08

Bmag = 0.38
Bang = math.radians(30)

F = Bmag * y_len * I * N

T = F * x_dist * math.cos(Bang)

print(0)
print(-T)
print(0)
