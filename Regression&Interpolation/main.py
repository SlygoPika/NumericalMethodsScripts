from math import *
from newtonInterpolation import *
from regression import *
from squareError import *
from normalEquationsRegression import *
from vandermondeInterpolation import *
from splineInterpolation import *


dataset = [(-2, 2.5), (0, 1), (1, 2.5), (2, 5.7), (3, 11.6)]


def model(x, a0, a1):
    return a0 + (a1 * (x ** 2))


def linearization_function(y):
    return log(y)


a0, a1 = least_square_fitting_coefficients(
    linearize_dataset(dataset, linearization_function), model)

a0 = e ** a0

print(root_mean_square_error(dataset, model, a0, a1))


# dataset = [(0 / 24, 15),
#            (1 / 24, 16),
#            (2 / 24, 15),
#            (3 / 24, 15),
#            (4 / 24, 15),
#            (5 / 24, 14),
#            (6 / 24, 14),
#            (7 / 24, 13),
#            (8 / 24, 13),
#            (9 / 24, 14),
#            (10 / 24, 13),
#            (11 / 24, 14),
#            (12 / 24, 15),
#            (13 / 24, 16),
#            (14 / 24, 18),
#            (15 / 24, 20),
#            (16 / 24, 21),
#            (17 / 24, 21),
#            (18 / 24, 21),
#            (19 / 24, 20),
#            (20 / 24, 19),
#            (21 / 24, 17),
#            (22 / 24, 16),
#            (23 / 24, 15),]
