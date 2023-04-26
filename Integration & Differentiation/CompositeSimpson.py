from math import *
from RichardsonError import *


def compositeSimpson(a, b, function, n):
    h = (b - a) / (n * 2)
    sum1 = 0
    sum2 = 0

    for i in range(1, n + 1):
        sum1 += function(a + (2 * i - 1) * h)

    for i in range(1, n):
        sum2 += function(a + 2 * i * h)

    return h / 3 * (function(a) + 4 * sum1 + function(b) + 2 * sum2)


def compositeSimpsonError(a, b, function, stepSize):
    iterations = int(1 / stepSize)

    result1 = compositeSimpson(a, b, function, int(iterations / 2))
    result2 = compositeSimpson(a, b, function, iterations)

    step1 = stepSize * 2

    return RichardsonError(result1, result2, step1, stepSize, 2)
