from math import *


def eulerMethod(function, initialCondition, step, finalEstimate):
    y = initialCondition[1]
    t = initialCondition[0]
    while t < finalEstimate:
        y += step * function(y, t)
        # print(y)
        t += step
    return y
