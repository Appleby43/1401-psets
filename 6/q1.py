import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

N_z = 3.82 * 10 ** -19

B_y_coeff = 2.12
v_x = 1.89
v_y = 4.7

# force / q = v cross b 

f_div_q = N_z / const.electron_charge

# only z component matters here - math from cross product def

B = f_div_q / (v_x * B_y_coeff - v_y) 
print(B)
