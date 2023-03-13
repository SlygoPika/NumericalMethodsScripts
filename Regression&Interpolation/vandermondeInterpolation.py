from math import *
import numpy as np


def vandermonde_interpolation_coefficients(dataset):
    arr = []
    res = []

    for x, y in dataset:
        temp = []

        for i in range(len(dataset)):
            temp.append(x**(i))

        arr.append(temp)
        res.append(y)

    matrix = np.array(arr)
    b = np.array(res).transpose()

    result = np.linalg.solve(matrix, b)

    return tuple(result)


def vandermonde_interpolation_value(dataset, x):
    coefficients = vandermonde_interpolation_coefficients(dataset)
    value = 0

    for i in range(len(coefficients)):
        value += coefficients[i] * x**(i)

    return value
