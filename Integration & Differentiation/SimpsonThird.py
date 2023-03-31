from math import *

def function(x):
    return cos(2 * x) * e ** (-2 * x)
    
def simpsonThird(a, b, function):
    h = (b - a) / 2
        
    return h / 3 * (function(a) + 4 * function((a + b) / 2) + function(b))


print(simpsonThird(1.4, 3.5, function))