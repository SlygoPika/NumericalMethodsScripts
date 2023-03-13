from math import *
import numpy as np
from inspect import signature


def least_square_fitting_coefficients(dataset, function):
    n = len(signature(function).parameters) - 1

    tempA = []
    tempB = []

    for x, y in dataset:
        arr = []

        for j in range(n):
            args = []
            for k in range(n):
                if k == j:
                    args.append(1)
                else:
                    args.append(0)

            arr.append(function(x, *args))

        tempA.append(arr)
        tempB.append(y)

    b = np.array(tempB).transpose()
    A = np.array(tempA)
    At = A.transpose()

    symm = np.dot(At, A)

    res = np.dot(At, b)

    coeffs = np.linalg.solve(symm, res)

    return tuple(coeffs)


def least_square_fitting_value(dataset, function, x):
    coefficients = least_square_fitting_coefficients(dataset, function)
    return function(x, *coefficients)
