from math import *


dictionary = {
    2: {
        "c": [1.0, 1.0],
        "x": [-0.5773502691896257, 0.5773502691896257]
    },
    3: {
        "c": [0.5555555555555556, 0.8888888888888888, 0.5555555555555556],
        "x": [-0.7745966692414834, 0.0, 0.7745966692414834]
    },
    4: {
        "c": [0.34785484513745385, 0.6521451548625461, 0.6521451548625461, 0.34785484513745385],
        "x": [-0.8611363115940526, -0.3399810435848563, 0.3399810435848563, 0.8611363115940526]
    }
}


def changeVariables(leftBound, rightBound, point):
    return ((rightBound - leftBound) * point + (rightBound + leftBound)) / 2


def gauss(func, leftBound, rightBound, points):
    c = dictionary[points]["c"]
    x = dictionary[points]["x"]
    sum = 0

    for i in range(0, points):
        sum += c[i] * func(changeVariables(leftBound,
                           rightBound, x[i])) * (rightBound - leftBound) / 2

    return sum


#print(gauss(function, leftBound, rightBound, points))
