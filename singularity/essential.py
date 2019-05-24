import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    z = x + y * 1j
    f = np.exp(1 / z)
    res = np.array(f, np.int64)
    print(res.shape)
    norm = abs(f)
    norm = np.clip(norm, 0, 3)
    print(norm.shape)
    return norm


x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.1, 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
ax = plt.axes(projection='3d')
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                cmap='hsv', edgecolor='none')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
ax.set_title('surface')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
