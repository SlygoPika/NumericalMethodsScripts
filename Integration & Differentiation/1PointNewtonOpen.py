from math import *

intervals = 8
a = 0
b = pi / 2

def function(x):
    return (1 - cos(x)) / (x**2)

def formula(function, a, b):
    return (b - a) * function((a + b) / 2)

def compositeNewtonCotes(function, a, b, n):
    h = (b - a) / n
    sum = 0

    for i in range(0, n):
        sum += formula(function, a + i * h, a + (i + 1) * h)

    return sum

print (compositeNewtonCotes(function, a, b, intervals))
