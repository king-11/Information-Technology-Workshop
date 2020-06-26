import numpy as np

a = np.ones((5, 5))

a[1:-1, 1:-1] = 0
print(a)
