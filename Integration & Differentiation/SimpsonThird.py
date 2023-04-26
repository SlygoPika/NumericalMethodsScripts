from math import *


def simpsonThird(a, b, function):
    h = (b - a) / 2

    return h / 3 * (function(a) + 4 * function((a + b) / 2) + function(b))
