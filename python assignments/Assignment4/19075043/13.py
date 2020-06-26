import numpy as np
import sys

a = np.array([(1, 2, 3)])

print("Size of the array: ", a.size)

print("Length of one array element in bytes: ", a.itemsize)

print("Total bytes consumed by the elements of the array: ", a.nbytes)
