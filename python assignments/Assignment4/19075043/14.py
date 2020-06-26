import numpy as np

b = [[1, 2, 3, 4], ['Red', 'Green', 'White', 'Orange'], [12.20, 15.0, 20.0, 40.0]]

a = np.array(b[0])
c = np.array(b[2])
b = np.array(b[1])


print(np.column_stack((a, b, c)))
