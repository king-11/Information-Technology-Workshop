import numpy as np

a = [float(x) for x in input().split()]

a = np.array(a)

a[0] = 0.
a[4] = 40.
print(a)
