import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

m_a = conv.g_to_kg(5.79)
m_b = conv.g_to_kg(8.45)
q = conv.uC_to_C(4.44)

d = 0.975

u = q ** 2 * const.k / d
print(u)

force = const.k * q * q / d ** 2 

print(force / m_a)
print(force / m_b)

v_a = math.sqrt( 2 * u * m_b / (m_a * (m_a + m_b)))
v_b = - (m_a / m_b) * v_a

print(v_a)
print(v_b)
