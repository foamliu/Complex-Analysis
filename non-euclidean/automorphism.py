import matplotlib.pyplot as plt
import numpy as np


def f(z):
    return np.exp(1j * theta) * (z - a) / (np.conjugate(a) * z - 1)


a = -0.7 + 0.2 * 1j
theta = np.pi / 4
fa = f(a)
f0 = f(0)

u = np.linspace(0, 1.0, 500)
v = np.linspace(0, 2 * np.pi, 3600)
uu, vv = np.meshgrid(u, v)
z = uu * np.exp(1j * vv)
w = f(z)
# T = np.arctan2(uu, vv)
T = np.sqrt(uu*vv)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(np.real(z), np.imag(z), c=T, s=10, lw=0, cmap='hsv')
plt.title('real points')
plt.grid(True)
plt.axis('equal')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.plot([np.real(a)], [np.imag(a)], 'ro')
plt.plot([0], [0], 'bo')

plt.subplot(1, 2, 2)
plt.scatter(np.real(w), np.imag(w), c=T, s=10, lw=0, cmap='hsv')
plt.title('f(z)=z**2')
plt.grid(True)
plt.axis('equal')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.plot([np.real(fa)], [np.imag(fa)], 'ro')
plt.plot([np.real(f0)], [np.imag(f0)], 'bo')

plt.show()
