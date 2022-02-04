def C_to_uC(c):
    return c * (10**6)

def mm_to_m(mm):
    return mm / 1000

def cm_to_m(cm):
    return cm / 100

'''Converts a number from picoUnits to units'''
def unpico(x):
    return x * 10 ** -12

'''Converts from base units to femtounits'''
def femto(x):
    return x * 10 ** 15
