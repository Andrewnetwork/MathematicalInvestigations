import numpy as np
from HeftyCounter import *

def listContinuity(path):
    deriv = []
    prev = path[0]
    prevSwitch = 0

    for elm in path:
        if elm == prev:
            deriv.append(prevSwitch)
        else:
            prevSwitch = int(not prevSwitch)
            deriv.append(prevSwitch)

        prev = elm

    return deriv


def binNum(len):
    hc = HeftyCounter(5,2)
    print(hc.counter)
    for x in range(1000):
        hc.increment(1)
        print(hc.counter)


def ternaryNum(len):
    hc = HeftyCounter(4, 3)
    print(hc.counter)
    for x in range(1000):
        hc.increment(1)
        print(hc.counter)

binNum(3)
