import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

q1 = conv.uC_to_C(2.6)
q2 = conv.uC_to_C(1.5)

def e(r, q_enc):
    return q_enc / (const.e_0 * 4 * math.pi * r * r)

print(e(5.3, q1 + q2))
print(e(.78, q1))
print(0)

def v(r, q_enc):
    return e(r, q_enc) * r

print(v(5.3, q1 + q2))
print(v(1.3, q1 + q2))
print(v(1.3, q2) + v(.78, q1))
print(v(1.3, q2) + v(.46, q1))
print(v(1.3, q2) + v(.46, q1))
print(v(1.3, q2) + v(.46, q1))
