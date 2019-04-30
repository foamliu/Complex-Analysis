import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(-1, 1, 80)
v = np.linspace(-np.pi, np.pi, 360)
uu, vv = np.meshgrid(u, v)
z0 = uu + 1j * vv
z = np.log(z0)
T = np.arctan2(uu, vv)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(uu, vv, c=T, s=10, lw=0, cmap='hsv')
plt.title('real points')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.xlim(-3, 3)
plt.ylim(-4, 4)
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(np.real(z), np.imag(z), c=T, s=10, lw=0, cmap='hsv')
plt.title('mapped points')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True)
plt.show()
