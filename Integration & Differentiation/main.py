from math import *
from Gauss import *
from TrapezoidQuadrature import *
from SimpsonThird import *
from RichardsonError import *
from RombergIntegration import *
from CompositeSimpson import *
from CompositeTrapezoid import *

leftBound = 1
rightBound = 2
desiredRomberg = (4, 3)


def function(x):
    return (e ** x - 1) / sin(x)

# print(RombergIntegrationTrapezoid(
#    function, leftBound, rightBound, desiredRomberg))


print(compositeSimpsonError(leftBound, rightBound, function, 10e-6))
