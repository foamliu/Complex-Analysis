import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(0, 1, 100)
v = np.linspace(0, np.pi, 360)
uu, vv = np.meshgrid(u, v)
z0 = uu * np.exp(1j * vv)
z = z0 ** 2
T = np.arctan2(uu, vv)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(np.real(z0), np.imag(z0), c=T, s=10, lw=0, cmap='hsv')
plt.title('real points')
plt.grid(True)
plt.axis('equal')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.subplot(1, 2, 2)
plt.scatter(np.real(z), np.imag(z), c=T, s=10, lw=0, cmap='hsv')
plt.title('mapped points')
plt.grid(True)
plt.axis('equal')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.show()
