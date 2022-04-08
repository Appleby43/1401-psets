import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

L = conv.unmicro(5.74)
R = conv.unkilo(1.46)
E = 16

tau = L / R

frac = .866
final_val = E / R

target_val = final_val * frac

# using i = E/R(1 - e^(-t/tau))
time = -tau * math.log(1 - (target_val * R / E)) 
print(time)

i = E / R * (1 - math.exp(-tau / tau))
print(i)
