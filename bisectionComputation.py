from math import log10


def compute(a, b, tol, equation):
    error = (b - a) / 2

    if (equation(a) > 0 and equation(b) > 0) or (equation(a) < 0 and equation(b) < 0):
        return -1

    while error > tol:
        midPoint = (a + b) / 2

        increasing = equation(a) < equation(b)
        midPointRes = equation(midPoint)

        if (midPointRes < 0 and increasing) or (midPointRes > 0 and (not increasing)):
            a = midPoint
        else:
            b = midPoint

        error = (b - a) / 2

    return (a + b) / 2, round((a + b) / 2, round(abs(log10(tol))))
