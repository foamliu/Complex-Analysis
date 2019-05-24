import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


u = np.linspace(0, np.pi, 30)
v = np.linspace(0, 2 * np.pi, 30)


x = np.outer(np.sin(u), np.sin(v))
print(x.shape)
y = np.outer(np.sin(u), np.cos(v))
print(y.shape)
z = np.outer(np.cos(u), np.ones_like(v))
print(z.shape)


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, color='b')
# ax.plot_wireframe(x, y, z)

plt.show()
