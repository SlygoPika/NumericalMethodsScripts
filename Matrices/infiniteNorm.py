import numpy as np
from math import *


def infiniteNorm(A):
    n1 = len(A)
    n2 = len(A[0])
    maxSum = 0

    for i in range(n1):
        sum = 0
        for j in range(n2):
            sum += abs(A[i][j])
        maxSum = max(maxSum, sum)

    return maxSum
