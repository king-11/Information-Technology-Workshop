import numpy as np

a = np.array([(10, 40), (30, 20)])

b = np.sort(a, axis=0, kind="mergesort")
print(b, end="\n\n")
c = np.sort(a, axis=1, kind="mergesort")
print(c, end="\n\n")

d = sorted(a.flatten())
print(d)
