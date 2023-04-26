from math import *

epsilon = 1e-10


def RKTrapezoid(function, initialCondition, step, finalEstimate):
    y = initialCondition[1]
    t = initialCondition[0]
    while t < finalEstimate:
        y += step * (function(y, t) + function(y +
                     step * function(y, t), t + step)) / 2
        # print(y)
        t += step + epsilon

    return y


def RKMidpoint(function, initialCondition, step, finalEstimate):
    y = initialCondition[1]
    t = initialCondition[0]
    while t < finalEstimate:
        y += step * function(y + (step / 2) * function(y, t), t + step / 2)
        # print(y)
        t += step + epsilon
    return y


def RK4Classic(function, initialCondition, step, finalEstimate):
    y = initialCondition[1]
    t = initialCondition[0]
    while t < finalEstimate:
        k1 = function(y, t)
        k2 = function(y + step * k1 / 2, t + step / 2)
        k3 = function(y + step * k2 / 2, t + step / 2)
        k4 = function(y + step * k3, t + step)
        y += step * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        # print(y)
        t += step + epsilon
    return y
