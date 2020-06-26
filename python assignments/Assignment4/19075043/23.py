import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

plt.close()


x = np.arange(1, 11)

y = np.random.randint(10, 100, 10)
plt.bar(x, y)
plt.show()
plt.close()

x = [21, 22, 23, 4, 5, 6, 77, 8, 9, 10, 31,
     32, 33, 34, 35, 36, 37, 18, 49, 50, 100]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins)
plt.show()
plt.close()

df = pd.read_csv("./LPPM-PLAT.csv")

df.plot(kind='line', x='EUR AM', y='USD AM')
plt.show()
plt.close()
