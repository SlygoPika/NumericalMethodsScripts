from math import *


def LagrangeInterpolation(dataset):
    def L(i, x):
        result = 1
        for j in range(len(dataset)):
            if j != i:
                result *= (x - dataset[j][0]) / (dataset[i][0] - dataset[j][0])
        return result

    def P(x):
        result = 0
        for i in range(len(dataset)):
            result += dataset[i][1] * L(i, x)
        return result

    return P
