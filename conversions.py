def C_to_uC(c):
    return c * (10**6)

def uC_to_C(uc):
    return uc / (10**6)

def mm_to_m(mm):
    return mm / 1000

def cm_to_m(cm):
    return cm / 100

def m2_to_cm2(m2):
    return m2 * 10000

def g_to_kg(g):
    return g / 1000

def mg_to_kg(mg):
    return mg / 10 ** 6

def micro(x):
    return x * 10 ** 6

def unmicro(x):
    return x * 10 ** -6

def pico(x):
    return x * 10 ** 12

'''Converts a number from picoUnits to units'''
def unpico(x):
    return x * 10 ** -12

'''Converts from base units to femtounits'''
def femto(x):
    return x * 10 ** 15

def unfemto(x):
    return x * 10 ** -15

def milli(x):
    return x * 1000

def unmilli(x):
    return x / 1000

def unkilo(x):
    return x * 1000

def kilo(x):
    return x / 1000
def mins_to_sec(mins):
    return mins * 60
