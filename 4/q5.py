import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv
import capacitor

C1 = conv.unmicro(11.7)
C2 = conv.unmicro(5.62)
C3 = conv.unmicro(4.48)

C12 = capacitor.parallel([C1, C2])
C123 = capacitor.series([C12, C3])
print(conv.micro(C123))
