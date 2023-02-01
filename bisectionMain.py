from math import *
import bisectionComputation

# VARIABLES TO FILL OUT
tolerance =     1e-14

leftGuess =     0.5
rightGuess =    1.5

def equation(x):
    return      2 + cos((e**x) - 2) - e**x


# OUTPUT

res = bisectionComputation.compute(leftGuess, rightGuess, tolerance, equation)
print(res)
