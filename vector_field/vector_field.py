import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(-5, 5, 200)
v = np.linspace(-5, 5, 200)
uu, vv = np.meshgrid(u, v)
z = uu + 1j * vv
w = np.power(z, 2)
T = np.arctan2(uu, vv)

fig = plt.figure()
ax = fig.add_subplot(111)
color = 2 * np.log(np.hypot(np.real(w), np.imag(w)))
ax.streamplot(np.real(z), np.imag(z), np.real(w), np.imag(w), color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
# ax.set_xlim(-2, 2)
# ax.set_ylim(-2, 2)
ax.set_aspect('equal')
plt.title('f(z)=z^2')
plt.show()
