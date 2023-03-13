from math import *


def cubic_spline_interpolation(dataset, x):
    # Find the interval
    for i in range(len(dataset) - 1):
        if dataset[i][0] <= x <= dataset[i + 1][0]:
            break

    # Find the coefficients
    a = dataset[i][1]
    b = (dataset[i + 1][1] - dataset[i][1]) / \
        (dataset[i + 1][0] - dataset[i][0])
    c = (dataset[i + 2][1] - dataset[i + 1][1]) / \
        (dataset[i + 2][0] - dataset[i + 1][0]) - b
    d = (c - b) / (dataset[i + 2][0] - dataset[i][0])

    return a + b * (x - dataset[i][0]) + c * (x - dataset[i][0]) ** 2 + d * (x - dataset[i][0]) ** 3


def linear_spline_interpolation_coefficients(dataset, x):
    # Find the interval
    for i in range(len(dataset) - 1):
        if dataset[i][0] <= x <= dataset[i + 1][0]:
            break

    # Find the coefficients
    a = dataset[i][1]
    b = (dataset[i + 1][1] - dataset[i][1]) / \
        (dataset[i + 1][0] - dataset[i][0])

    return a, b


def linear_spline_interpolation_value(dataset, x):
    for i in range(len(dataset) - 1):
        if dataset[i][0] <= x <= dataset[i + 1][0]:
            break

    a, b = linear_spline_interpolation_coefficients(dataset)

    return a + b * (x - dataset[i][0])
