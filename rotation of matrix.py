import numpy as np

x = np.arange(1,10).reshape(3, 3)
print(x)
i = np.array([0, 1, 2, 5, 8, 7, 6, 3])
x.flat[i] = np.roll(x.flat[i], 1)
print(x)
