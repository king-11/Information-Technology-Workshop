import pandas as pd

a = list(range(2, 12, 2))
b = list(range(1, 11, 2))
a = pd.Series(a)
b = pd.Series(b)


print(a.add(b), a.sub(b), a.mul(b), a.div(b))
