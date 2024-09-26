import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(X, Y)

plt.scatter(np.arange(5), np.arange(5))

plt.xticks(())
plt.yticks(())

plt.show()