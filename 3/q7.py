import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

q1_r = 8.1
q2_r = 2 * q1_r
q3_r = q1_r

q1 = conv.unpico(4.69)
q2 = 4.8 * q1
q3 = -2.3 *  q1

def potential(q, r):
    return const.k * q / r

total = potential(q1, q1_r) + potential(q2, q2_r) + potential(q3, q3_r)

print(total)
