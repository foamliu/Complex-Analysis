from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=plt.figaspect(1))
fig.set_size_inches([8,8])
ax = fig.add_subplot(111, projection='3d')

#r=1

# values for extents of meshes
begp = 0.25
endp = 1+begp
extp = endp+1

u = np.linspace(-2, 2, 200)
#v = np.linspace(0, 2*np.pi, 60)
v = np.linspace(begp*np.pi, endp*np.pi, 30)
[u,v] = np.meshgrid(u,v)

u2 = np.linspace(-2, 2, 200)
v2 = np.linspace(endp*np.pi, extp*np.pi, 30)
[uu2, vv2] = np.meshgrid(u2, v2)

a = 1
b = 1
c = 1

# surface 1
x = a*np.cosh(u)*np.cos(v)
y = b*np.cosh(u)*np.sin(v)
z = c*np.sinh(u)

# surface 2
x2 = a*np.cosh(uu2)*np.cos(vv2)
y2 = b*np.cosh(uu2)*np.sin(vv2)
z2 = c*np.sinh(uu2)

# plot surface 1 in red / surface 2 in blue
ax.plot_surface(x, y, z, rstride=4, cstride=4, color='red', edgecolor='gray')
ax.plot_surface(x2, y2, z2, rstride=4, cstride=4, color='blue', edgecolor='lightgray')

# set viewing angle + perspactive to get best image
ax.azim = 313   # z rotation (default=270)
ax.elev = 16    # x rotation (default=0)
ax.dist = 8    # zoom (define perspective)
ax.set_axis_off()
plt.show()