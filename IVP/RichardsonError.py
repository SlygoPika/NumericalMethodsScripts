from math import *


def RichardsonError(Ih1, Ih2, h1, h2, order):
    if h1 < h2:
        print("step1 must be greater than step2")
        return -1

    return (Ih2 - Ih1) / ((h1 / h2) ** order - 1)
