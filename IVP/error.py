from math import *
from RichardsonError import RichardsonError
from euler import eulerMethod
from RungeKutta import RKMidpoint, RKTrapezoid, RK4Classic


def eulerError(function, initialCondition, step1, step2, finalEstimate):
    result1 = eulerMethod(function, initialCondition, step1, finalEstimate)
    result2 = eulerMethod(function, initialCondition, step2, finalEstimate)
    ORDER = 1
    return abs(RichardsonError(result1, result2, step1, step2, ORDER))


def RKTrapezoidError(function, initialCondition, step1, step2, finalEstimate):
    result1 = RKTrapezoid(function, initialCondition, step1, finalEstimate)
    result2 = RKTrapezoid(function, initialCondition, step2, finalEstimate)
    ORDER = 2
    return abs(RichardsonError(result1, result2, step1, step2, ORDER))


def RKMidpointError(function, initialCondition, step1, step2, finalEstimate):
    result1 = RKMidpoint(function, initialCondition, step1, finalEstimate)
    result2 = RKMidpoint(function, initialCondition, step2, finalEstimate)
    ORDER = 2
    return abs(RichardsonError(result1, result2, step1, step2, ORDER))


def RK4ClassicError(function, initialCondition, step1, step2, finalEstimate):
    result1 = RK4Classic(function, initialCondition, step1, finalEstimate)
    result2 = RK4Classic(function, initialCondition, step2, finalEstimate)
    ORDER = 4
    return abs(RichardsonError(result1, result2, step1, step2, ORDER))
