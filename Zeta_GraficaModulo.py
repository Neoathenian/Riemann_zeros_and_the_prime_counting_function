"""Makes the ModuloZeta.svg plot."""
from mpmath import zeta
import matplotlib.pyplot as plt
import numpy as np

# Create the grid
x = np.linspace(-1, 0.50, 50)
y = np.linspace(0, 40, 400)
X, Y = np.meshgrid(x, y)

# Calculate Z values
Z = np.array([[float(abs(zeta(complex(x0, y0)))) for x0 in x] for y0 in y])

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.zaxis.set_rotate_label(False)  # disable automatic rotation
ax.set_zlabel('$|\zeta(x+iy)|$', rotation=90)
ax.set_zlim3d(0, 17.5)

# Plot the surface
ax.plot_surface(X, Y, Z)
plt.show()
