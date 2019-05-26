import matplotlib.pyplot as plt
import numpy as np


def f(z):
    return (z - a) * (z - b) / (z - c)


epsilon = 1e-6
a = -0.7 + 0.2 * 1j
b = 0.5 + (-0.3) * 1j
c = 1.5 + 0.5 * 1j
fa = f(a)
fb = f(b)
# fc = f(c)
f1 = f(2)

t = np.linspace(0, 2 * np.pi, 3600)
uu = 2 * np.cos(t)
vv = 2 * np.sin(t)
z0 = uu + 1j * vv
z = f(z0)

T = np.arctan2(uu, vv)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(uu, vv, c=T, s=3, lw=0, cmap='hsv')
plt.title('original(z) plane')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.axis('equal')
plt.grid(True)
plt.plot([np.real(a), np.real(b), np.real(c)], [np.imag(a), np.imag(b), np.imag(c)], 'ro')
plt.plot([2], [0], 'bo')

plt.text(np.real(a), np.imag(a), 'a', fontsize=12)
plt.text(np.real(b), np.imag(b), 'b', fontsize=12)
plt.text(np.real(c), np.imag(c), 'c', fontsize=12)

plt.subplot(1, 2, 2)
plt.scatter(np.real(z), np.imag(z), c=T, s=3, lw=0, cmap='hsv')
plt.title(' f(z)=(z-a)*(z-b)/(z-c)')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.axis('equal')
plt.grid(True)
plt.plot([np.real(fa), np.real(fb)], [np.imag(fa), np.imag(fb)], 'ro')
plt.plot([np.real(f1)], [np.imag(f1)], 'bo')

plt.show()
