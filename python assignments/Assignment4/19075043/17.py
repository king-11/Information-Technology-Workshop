import numpy as np
import pandas as pd

a = np.arange(10, 60, 10, dtype=np.int64)

p = pd.DataFrame(a, dtype=np.int64)
print(p)
