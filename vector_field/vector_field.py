import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(-3, 3, 25)
v = np.linspace(-3, 3, 25)
uu, vv = np.meshgrid(u, v)
z = uu + 1j * vv
# w = 1/z
# w = np.exp(z)
# w = np.log(z)
w = np.sin(z)
T = np.arctan2(uu, vv)

fig = plt.figure()
ax = fig.add_subplot(111)
color = 2 * np.log(np.hypot(np.real(w), np.imag(w)))
# ax.streamplot(np.real(z), np.imag(z), np.real(w), np.imag(w), color=color, linewidth=1, cmap=plt.cm.inferno,
#               density=2, arrowstyle='->', arrowsize=1.5)

Q = plt.quiver(np.real(z), np.imag(z), np.real(w), np.imag(w), units='width')
qk = plt.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
# ax.set_xlim(-2, 2)
# ax.set_ylim(-2, 2)
ax.set_aspect('equal')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
# plt.title('f(z)=1/z')
# plt.title('f(z)=exp(z)')
# plt.title('f(z)=log(z)')
plt.title('f(z)=sin(z)')
plt.show()
