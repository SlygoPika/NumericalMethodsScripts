from math import *


def square_error(dataset, function, *argv):
    squareError = 0

    for x, y in dataset:
        error = y - function(x, *argv)
        squareError += error**2

    return squareError


def mean_square_error(dataset, function, *argv):
    return square_error(dataset, function, *argv) / len(dataset)


def root_mean_square_error(dataset, function, *argv):
    return sqrt(mean_square_error(dataset, function, *argv))


def linearize_dataset(dataset, linearization_function):
    new_dataset = []

    for x, y in dataset:
        new_dataset.append((x, linearization_function(y)))

    return new_dataset
