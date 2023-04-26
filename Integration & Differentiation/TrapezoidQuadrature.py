from math import *


def trapezoid(a, b, function):
    return (b - a) * (function(a) + function(b)) / 2
