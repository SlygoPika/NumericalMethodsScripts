from math import *


def RichardsonError(Ih1, Ih2, h1, h2, order):
    return (Ih2 - Ih1) / ((h1 / h2) ** order - 1)
