from math import *
from euler import eulerMethod
from RichardsonError import RichardsonError
from error import eulerError, RKTrapezoidError, RKMidpointError, RK4ClassicError
from RungeKutta import RKMidpoint, RKTrapezoid, RK4Classic


step1 = 1e-3
step2 = 0.5
initialCondition = (0, 1)
finalEstimate = 1


def function(y, t):
    return 2 * (t + 1) * y


print(RKTrapezoidError(function, initialCondition, step1 * 2, step1, finalEstimate))

# eulerMethod(function, initialCondition, step, finalEstimate)
