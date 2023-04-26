import scipy
import scipy.linalg
from math import *
import pprint
import numpy as np

from palu import PALU, ALU


def GaussElimPALU(A, res):
    P, L, U = PALU(A)

    d = scipy.linalg.solve(L, np.matmul(P, res))
    print("d:")
    pprint.pprint(d)

    x = scipy.linalg.solve(U, d)
    print("x:")
    pprint.pprint(x)

    return x


def GaussElimALU(A, res):
    L, U = ALU(A)

    d = scipy.linalg.solve(L, res)
    print("d:")
    pprint.pprint(d)

    x = scipy.linalg.solve(U, d)
    print("x:")
    pprint.pprint(x)

    return x
