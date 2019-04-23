import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d
def f(x, y):
    z = x + y*1j
    f = 1/ (1+np.power(z,2))
    # res = np.array(f, np.int64)
    norm = abs(f)
    norm = np.clip(norm, 0, 8)
    return norm

x = np.linspace(-3., 3., 50)
y = np.linspace(-3., 3., 50)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim(-3., 3.)
ax.set_ylim(-3., 3.)
ax.set_zlim(0, 6)
plt.show()