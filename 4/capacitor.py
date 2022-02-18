'''Finds the total capacitance of capacitors in series'''
def series(capacitors):
    total = 0
    for cap in capacitors:
       total += (1 / cap)
    return 1 / total

def parallel(capacitors):
    total = 0
    for cap in capacitors:
        total += cap
    return total

