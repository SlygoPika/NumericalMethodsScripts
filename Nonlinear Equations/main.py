from falsePosition import falsePosition
import bisectionComputation
from math import *

tolerance = 1e-10

leftGuess = 0
rightGuess = 0.5


def equation(x):
    return sin(e ** (3 * x) + 4) - 0.5


print(bisectionComputation.compute(leftGuess, rightGuess, tolerance, equation))
