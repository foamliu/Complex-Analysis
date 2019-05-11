import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

filename = '../images/yangmi.jpg'
img = mpimg.imread(filename)
img = img[:, :, 0]
height, width = img.shape[:2]
print(img.shape)
u = np.arange(0, width)
v = np.arange(0, height)
uu, vv = np.meshgrid(u, v)
print(uu.shape)
z0 = uu + 1j * vv
z = (1j * z0 + 1) / (z0 + 1j)
T = np.reshape(img, (height*width))

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(uu, vv, c=T, s=10, lw=0, cmap=None)
plt.title('real points')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.axis('equal')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(np.real(z), np.imag(z), c=T, s=10, lw=0, cmap='hsv')
plt.title('poincare disk')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.axis('equal')
plt.grid(True)
plt.show()
