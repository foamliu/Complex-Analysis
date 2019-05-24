import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

filename = '../images/dilireba.jpg'
img = mpimg.imread(filename)
img = img/255.
height, width = img.shape[:2]
print(img.shape)
print(np.max(img))
u = np.linspace(-0.5, 0.5, width)
v = np.linspace(1, 0, height)
uu, vv = np.meshgrid(u, v)
uu = uu.flatten()
vv = vv.flatten()
print(uu.shape)
z0 = uu + 1j * vv
z = (1j * z0 + 1) / (z0 + 1j)
# T = np.arctan2(uu, vv)
img = np.reshape(img, (-1, 3))
print(img.shape)

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(uu, vv, c=img, s=10, lw=0, cmap=None)
plt.title('real points')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.axis('equal')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(np.real(z), np.imag(z), c=img, s=10, lw=0, cmap='hsv')
plt.title('poincare disk')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.axis('equal')

plt.grid(True)
plt.show()
