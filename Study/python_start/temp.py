import numpy as np

x = np.random.randn(100)
y = np.random.randn(100)

x = np.dot(x.T, x)
print(x[0,0])
