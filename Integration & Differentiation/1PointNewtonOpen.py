from math import *


def formula(function, a, b):
    return (b - a) * function((a + b) / 2)


def compositeNewtonCotes(function, a, b, n):
    h = (b - a) / n
    sum = 0

    for i in range(0, n):
        sum += formula(function, a + i * h, a + (i + 1) * h)

    return sum
