
from math import *
from RichardsonError import *


def trapezoid(a, b, function):
    return (b - a) * (function(a) + function(b)) / 2


def compositeTrapezoid(a, b, function, n):
    h = (b - a) / n
    sum = 0

    for i in range(1, n):
        sum += function(a + i * h)

    return h / 2 * (function(a) + 2 * sum + function(b))


def compositeSimpsonError(a, b, function, stepSize):
    iterations = int(1 / stepSize)

    result1 = compositeTrapezoid(a, b, function, int(iterations / 2))
    result2 = compositeTrapezoid(a, b, function, iterations)

    step1 = stepSize * 2

    return RichardsonError(result1, result2, step1, stepSize, 2)
