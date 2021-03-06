import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(-2, 2, 200)
v = np.linspace(-2, 2, 200)
uu, vv = np.meshgrid(u, v)
z0 = uu + 1j * vv
z = 1 / (1 + z0 ** 2)
T = np.arctan2(uu, vv)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(uu, vv, c=T, s=10, lw=0, cmap='hsv')
plt.title('real points')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(np.real(z), np.imag(z), c=T, s=10, lw=0, cmap='hsv')
plt.title('f(z)=1/(1+z^2)')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.grid(True)
plt.show()
