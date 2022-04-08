import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

L1 = conv.unmilli(51)
L2 = conv.unmilli(70)

N1 = 119
N2 = 233

M = conv.unmilli(6.2)
i1 = conv.unmilli(8.7)
di1 = 4.2 

flux = L1 * i1 / N1
print(conv.micro(flux))

self_ind = L1 * di1
print(conv.milli(self_ind)) 

flux21 = M * i1 / N2
print(conv.nano(flux21))

E2 = M * di1
print(conv.milli(E2))
