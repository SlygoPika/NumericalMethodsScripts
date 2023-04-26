from math import *
from euler import eulerMethod
from RichardsonError import RichardsonError
from error import eulerError, RKTrapezoidError, RKMidpointError, RK4ClassicError
from RungeKutta import RKMidpoint, RKTrapezoid, RK4Classic


step1 = 0.1
step2 = 0.5
initialCondition = (-8.09, -2.79)
finalEstimate = -7.09


def function(y, t):
    return 5.96 * cos(t)


print(eulerMethod(function, initialCondition, step1, finalEstimate))

# eulerMethod(function, initialCondition, step, finalEstimate)
