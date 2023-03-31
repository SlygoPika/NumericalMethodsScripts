
from math import *

intervals = 3

def function(x):
    return e ** (-4 * x) * sin(3 * x) / (x ** 2 + 4)

def trapezoid(a, b, function):
    return (b - a) * (function(a) + function(b)) / 2

def compositeTrapezoid(a, b, function, n):
    h = (b - a) / n
    sum = 0

    for i in range(1, n):
        sum += function(a + i * h)

    return h / 2 * (function(a) + 2 * sum + function(b))

print(compositeTrapezoid(-2, 3, function, intervals))
