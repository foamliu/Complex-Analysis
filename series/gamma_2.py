import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import mpmath
mpmath.dps = 5

def f(x, y):
    z = x + y * 1j
    f = mpmath.gamma(z)
    norm = abs(f)
    norm = np.clip(norm, 0, 4)
    return norm


x = np.linspace(-4., 4., 100)
y = np.linspace(-2., 2., 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hsv', edgecolor='none')
# ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)
ax.set_title('f(z)=sin(z)')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# ax.set_xlim(-3., 3.)
# ax.set_ylim(-3., 3.)
ax.set_zlim(0, 4)
plt.show()
