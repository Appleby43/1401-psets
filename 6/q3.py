import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

V = conv.unkilo(122)
R = 1.34
q = 3.2 * 10 ** -19
m = 3.92 * 10 ** -25

Ke = V * q 
velo = math.sqrt(2 * Ke / m)

# given circular motion eq, r = mv / qB

B = m * velo / (q * R) 
print(B)

sample_mass = conv.mg_to_kg(0.808)
mass_per_time = sample_mass / conv.mins_to_sec(60)

I = (mass_per_time / m) * q

print(I)

#recall that each particle has Ke = Vq

total_particles_per_hr = sample_mass / m

print(total_particles_per_hr * Ke * 1.42)
