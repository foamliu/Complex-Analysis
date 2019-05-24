import matplotlib.pyplot as plt
import numpy as np

nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)

plt.scatter(xv, yv, color=[1.0, 0.5, 0.5])
plt.show()
