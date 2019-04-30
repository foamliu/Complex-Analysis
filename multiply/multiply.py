import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(1, 3, 80)
v = np.linspace(1, 3, 80)
uu, vv = np.meshgrid(u, v)
z0 = uu + 1j * vv
m = 2 + 3j
z = z0 * m
T = np.arctan2(uu, vv)
print(T)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(uu, vv, c=T, s=10, lw=0, cmap='hsv')
plt.title('real points')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(np.real(z), np.imag(z), c=T, s=10, lw=0, cmap='hsv')
plt.title('mapped points')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.grid(True)
plt.show()
