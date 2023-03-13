from math import *
from newtonInterpolation import *
from regression import *
from squareError import *
from normalEquationsRegression import *
from vandermondeInterpolation import *


dataset = [(-2, 2), (1, -1), (3, 1)]


def model(x, a0, a1):
    return a0 + a1 * sin(x)


def linearization_function(y):
    return y ** -1


print(square_error(dataset, model, -0.5, 1.7))


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
