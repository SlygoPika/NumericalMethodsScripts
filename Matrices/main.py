from GaussElim import *
from infiniteNorm import *
from conditioningNum import *

import scipy
import scipy.linalg
import numpy as np


A = np.array(
    [[1, 1, 0],
     [0, 1, 1],
     [1, 2, 1],
     [1, 4, -2]])

At = A.transpose()

print(At)

AtxA = np.matmul(At, A)

res = np.array([2, 3, -1, 4]).transpose()

AtxRes = np.matmul(At, res)

# print(np.matmul(A, GaussElimPALU(AtxA, AtxRes)))

print(np.matmul(A, np.linalg.solve(AtxA, AtxRes)))

# mat = np.array([[2, -1, 1],
#                 [1, 0, 1],
#                 [3, -1, 4]])
# print(conditioningNum(mat))

#GaussElimPALU(AtxA, AtxRes)
