import numpy as np
from math import pi

a = list(map(int, input().split()))
b = np.array(a)

b = b / 180 * pi
print(np.sin(b))
print(np.cos(b))
print(np.tan(b))
