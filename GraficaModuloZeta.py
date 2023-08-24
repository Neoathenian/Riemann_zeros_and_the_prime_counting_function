"""This script creates a plot of the modulus of the zeta function (I only kept this one cause I like it)(pretty useless script)"""

from mpmath import *
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 0.50, 50)
y = np.linspace(0, 40, 400)
X, Y = np.meshgrid(x, y)


Z=np.array([[float(abs(zeta(complex(x0,y0)))) for x0 in x] for y0 in y])


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.zaxis.set_rotate_label(False)  # disable automatic rotation
ax.set_zlabel('$|\zeta(x+iy)|$',rotation=90)



ax.set_zlim3d(0,17.5)
#ax.view_init(10, 10)
plt.show()

