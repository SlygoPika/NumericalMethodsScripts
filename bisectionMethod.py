from math import *

tolerance = 1e-14

leftGuess = 0.5
rightGuess = 1.5


def equation(x):
    return 2 + cos((e**x) - 2) - e**x


error = (rightGuess - leftGuess) / 2

while error >= tolerance:
    midPoint = (leftGuess + rightGuess) / 2

    increasing = equation(leftGuess) < equation(rightGuess)
    midPointRes = equation(midPoint)

    if (midPointRes < 0 and increasing) or (midPointRes > 0 and (not increasing)):
        leftGuess = midPoint
    else:
        rightGuess = midPoint

    error = (rightGuess - leftGuess) / 2

print(round((leftGuess + rightGuess) / 2, round(abs(log10(tolerance)))))
