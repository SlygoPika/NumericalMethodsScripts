from math import *
from CompositeTrapezoid import *
from RichardsonError import *


def RombergIntegrationTrapezoid(function, leftBound, rightBound, desiredResult):
    R_x_1 = []

    if desiredResult[0] < desiredResult[1]:
        print("Error: Desired result is not possible")
        return None

    for i in range(0, desiredResult[0]):
        R_x_1.append(compositeTrapezoid(leftBound, rightBound, function, 2**i))

    print(R_x_1)

    newCol = []
    currentCol = R_x_1
    for j in range(0, desiredResult[1]):
        if j + 1 == desiredResult[1]:
            return currentCol[desiredResult[0] - 1 - j]

        newCol = []
        for i, r in enumerate(currentCol):
            if i == 0:
                continue

            newR = (2 ** (2 * (j + 1)) * r -
                    currentCol[i - 1]) / (2 ** (2 * (j + 1)) - 1)

            newCol.append(newR)

        currentCol = newCol
        # print(currentCol)
