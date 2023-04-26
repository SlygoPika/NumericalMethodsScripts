from math import *
import bisectionComputation

# VARIABLES TO FILL OUT
tolerance = 10e-7

leftGuess = -1
rightGuess = 1


def equation(x):
    return 2.5 * (x ** 4) + 10.6 * (x ** 3) + 5.4 * (x ** 2) + 10.6 * x + 2.9


# OUTPUT

res = bisectionComputation.compute(leftGuess, rightGuess, tolerance, equation)
print(res)
