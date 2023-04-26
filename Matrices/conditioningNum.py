import numpy as np
from math import *
from infiniteNorm import infiniteNorm


def conditioningNum(A):
    return infiniteNorm(A) * infiniteNorm(np.linalg.inv(A))
