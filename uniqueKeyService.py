import math

currentKey = 0

def requestUniqueKey():
    global currentKey
    currentKey += 1
    return currentKey