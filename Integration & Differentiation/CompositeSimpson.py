from math import *

intervals = 4

def function(x):
    return 1 / x

def compositeSimpson(a, b, function, n):
    h = (b - a) / (n * 2)
    sum1 = 0
    sum2 = 0

    for i in range(1, n + 1):
        sum1 += function(a + (2 * i - 1) * h)
    
    for i in range(1, n):
        sum2 += function(a + 2 * i * h)

    return h / 3 * (function(a) + 4 * sum1 + function(b) + 2 * sum2)

print (compositeSimpson(1, 7, function, intervals))