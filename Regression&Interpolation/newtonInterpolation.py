from math import *


def newton_interpolation_coefficients(dataset):
    # Find the coefficients
    coefficients = []
    for i in range(len(dataset)):
        coefficients.append(dataset[i][1])

    for i in range(1, len(dataset)):
        for j in range(len(dataset) - 1, i - 1, -1):
            coefficients[j] = (coefficients[j] - coefficients[j - 1]
                               ) / (dataset[j][0] - dataset[j - i][0])

    # Find the value

    return tuple(coefficients)


def newton_interpolation_value(dataset, x):
    coefficients = newton_interpolation_coefficients(dataset)
    value = 0

    for i in range(len(coefficients)):
        temp = 1

        for j in range(i):
            temp *= (x - dataset[j][0])

        value += coefficients[i] * temp

    return value
