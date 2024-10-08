import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = 2**x + 1

plt.figure(num = 3, figsize=(8, 5))
plt.plot(x, y1)
plt.plot(x, y2, 
         color= 'red',
         linewidth= 1.0,
         linestyle='--'
        )

plt.xlabel("I am x")
plt.ylabel("I am y")
plt.title("With Labels")

plt.show()