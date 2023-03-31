from math import *

def function(x):
    return e ** (-3.4 * x ** 2)

def trapezoid(a, b, function):
    return (b - a) * (function(a) + function(b)) / 2

print(trapezoid(1.6, 8.1, function))