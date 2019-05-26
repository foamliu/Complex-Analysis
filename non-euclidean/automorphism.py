import matplotlib.pyplot as plt
import numpy as np


def f(z):
    return np.exp(1j * phi) * (z - a) / (1 - np.conjugate(a) * z)


a = -0.7 + 0.2 * 1j
phi = np.pi / 4
p = np.exp(1j * phi)
fa = f(a)
f0 = f(0)
fp = f(p)
f1 = f(1)

u = np.linspace(0, 1.0, 500)
v = np.linspace(0, 2 * np.pi, 3600)
uu, vv = np.meshgrid(u, v)
z = uu * np.exp(1j * vv)
w = f(z)
# T = np.arctan2(uu, vv)
T = np.sqrt(uu * vv)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(np.real(z), np.imag(z), c=T, s=10, lw=0, cmap='hsv')
plt.title('real points')
plt.grid(True)
plt.axis('equal')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.plot([np.real(a)], [np.imag(a)], 'ro')
plt.text(np.real(a), np.imag(a), 'a', fontsize=12)
plt.plot([np.real(p)], [np.imag(p)], 'ro')
plt.text(np.real(p), np.imag(p), 'p', fontsize=12)
plt.plot([0], [0], 'ro')
plt.text(0, 0, '0', fontsize=12)
plt.plot([1], [0], 'ro')
plt.text(1, 0, '1', fontsize=12)

plt.subplot(1, 2, 2)
plt.scatter(np.real(w), np.imag(w), c=T, s=10, lw=0, cmap='hsv')
plt.title(r'f(z)=$\exp(i \phi)\frac{z-a}{1-\bar a z} (\phi=\pi / 4$)')
plt.grid(True)
plt.axis('equal')
plt.xlabel('Re(w)')
plt.ylabel('Im(w)')
plt.plot([np.real(fa)], [np.imag(fa)], 'ro')
plt.text(np.real(fa), np.imag(fa), 'f(a)', fontsize=12)
plt.plot([np.real(fp)], [np.imag(fp)], 'ro')
plt.text(np.real(fp), np.imag(fp), 'f(p)', fontsize=12)
plt.plot([np.real(f0)], [np.imag(f0)], 'ro')
plt.text(np.real(f0), np.imag(f0), 'f(0)', fontsize=12)
plt.plot([np.real(f1)], [np.imag(f1)], 'ro')
plt.text(np.real(f1), np.imag(f1), 'f(1)', fontsize=12)

plt.show()
