import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d
def f(x, y):
    z = x + y*1j
    f = np.sin(z)
    res = np.array(f, np.int64)
    print(res.shape)
    norm = abs(f)
    print(norm.shape)
    return norm

x = np.linspace(0., np.pi, 100)
y = np.linspace(0., 1., 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='hsv', edgecolor='none')
ax.set_title('surface')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()