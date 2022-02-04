import math
import numpy as np

import sys
sys.path.append('../')

import constants as const

edge_length = 1.96
area = edge_length**2

print(0)

b_magnitude = 2.24
print(-b_magnitude * area)

c_vector = np.array([-3.94, 0, 3.2])
normal_vec = np.array([0, area, 0])

flux = np.dot(c_vector, normal_vec)
print(np.linalg.norm(flux))

print(0)
