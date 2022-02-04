import math

import sys
sys.path.append('../')

import constants as const

initial_velo = 5.67 * 10**6
angle = math.radians(41.9)
E = 3.4
dist_to_screen = 3.23

x_comp = math.cos(angle) * initial_velo
y_comp_initial = math.sin(angle) * initial_velo

time_to_collision = dist_to_screen / x_comp 

force = E * const.electron_charge
acceleration = force / const.electron_mass

y_comp_final = y_comp_initial + time_to_collision * acceleration

print(y_comp_final)
