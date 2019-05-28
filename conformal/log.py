import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(0.5, 1, 100)
v = np.linspace(0, np.pi/2, 360)
uu, vv = np.meshgrid(u, v)
z0 = uu * np.exp(1j * vv)
z = np.log(z0)
T = np.arctan2(uu, vv)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(np.real(z0), np.imag(z0), c=T, s=10, lw=0, cmap='hsv')
plt.title('real points')
plt.grid(True)
plt.axis('equal')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')

plt.subplot(1, 2, 2)
plt.scatter(np.real(z), np.imag(z), c=T, s=10, lw=0, cmap='hsv')
plt.title('f(z)=log(z)')
plt.grid(True)
plt.axis('equal')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')

plt.show()
