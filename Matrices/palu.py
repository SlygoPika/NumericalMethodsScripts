import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library


def PALU(A):

    P, L, U = scipy.linalg.lu(A)
    print("P:")
    pprint.pprint(P)

    print("L:")
    pprint.pprint(L)

    print("U:")
    pprint.pprint(U)

    return P, L, U


def ALU(A):
    L, U = scipy.linalg.lu(A, permute_l=True)

    print("L:")
    pprint.pprint(L)

    print("U:")
    pprint.pprint(U)

    return L, U
