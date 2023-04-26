from math import *
from matrixFunctions import *
import numpy as np

matrix = np.array([[1, 1, 0, 0], [0, 1, 1, 0], [1, 2, 1, 0], [1, 4, -2, 0]])

result = np.array([2, 3, -1, 4]).transpose()

test1 = np.array([-3.3, 1.9, 11.5]).transpose()
test2 = np.array([6.1, -0.1, 6.5]).transpose()
test3 = np.array([4.1, 4.0, 5.5]).transpose()
test4 = np.array([3.5, 4.5, 4.5]).transpose()

vector = np.linalg.solve(matrix, result)

print(vector)
