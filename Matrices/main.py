from GaussElim import *

import scipy
import scipy.linalg
import numpy as np

A = np.array(
    [[3, -2, 4],
     [-6, 3, -3],
     [18, -14, 41]])

res = np.array([-16, 30, -100]).transpose()

GaussElimPALU(A, res)
