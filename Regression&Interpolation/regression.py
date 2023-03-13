from math import *
from squareError import *


def linear_regression_coefficients(dataset):
    # Find the coefficients
    xysum = 0
    xsum = 0
    ysum = 0
    x2sum = 0

    for x, y in dataset:
        newy = y
        xysum += x * newy
        xsum += x
        ysum += newy
        x2sum += x ** 2

    a1 = (len(dataset) * xysum - xsum * ysum) / \
        (len(dataset) * x2sum - xsum ** 2)
    a0 = (ysum - a1 * xsum) / len(dataset)

    return a0, a1


def linear_regression_value(x, a0, a1):
    return a0 + a1 * x
