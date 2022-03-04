'''Finds the total resistence of resistors in series'''
def series(resistors):
    total = 0
    for res in resistors:
        total += res
    return total
 
def parallel(resistors):
   total = 0
    for res in resistors:
       total += (1 / res)
    return 1 / total


