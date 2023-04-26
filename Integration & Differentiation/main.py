from math import *
from Gauss import *
from TrapezoidQuadrature import *
from SimpsonThird import *
from RichardsonError import *
from RombergIntegration import *
from CompositeSimpson import *
from CompositeTrapezoid import *

# leftBound = 1
# rightBound = 1.5
# desiredRomberg = (4, 3)

# leftBound = 1
# rightBound = 3
# desiredRomberg = (4, 3)


# def function(x):
#     return e ** (- (x ** 2))


# def function(x):
#     return x ** 2 * log(x)

# print(RombergIntegrationTrapezoid(
#    function, leftBound, rightBound, desiredRomberg))


# print(gauss(function, leftBound, rightBound, 2))

leftBound = 0
rightBound = 2 * sqrt(3)
desiredRomberg = (4, 4)


def function(x):
    return 1 / sqrt(x**2 + 4)


print(RombergIntegrationTrapezoid(
    function, leftBound, rightBound, desiredRomberg))
