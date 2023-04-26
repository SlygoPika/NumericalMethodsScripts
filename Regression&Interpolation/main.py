from math import *
from newtonInterpolation import *
from regression import *
from squareError import *
from normalEquationsRegression import *
from vandermondeInterpolation import *
from splineInterpolation import *

# Q6
dataset6 = [(1, 0.7), (2, 3.7), (3, 12.9)]
x6 = 2.5


def model(x, a0, a1):
    return a0 + (a1 * x)


def linearization_function(y):
    return (y)


# a0, a1 = least_square_fitting_coefficients(
#     linearize_dataset(dataset, linearization_function), model)

# a0 = e ** a0

print(newton_interpolation_coefficients(dataset6))
# print(root_mean_square_error(dataset, model, a0, a1))
