from mpmath import *
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.type_check import imag, real

n=1000
x = np.linspace(0,100,n)
zer=np.zeros(n)


y=np.array([float(abs(zeta(1/2+1j*x0))) for x0 in x])
yreal=np.array([float(real(zeta(1/2+1j*x0))) for x0 in x])
yimag=np.array([float(imag(zeta(1/2+1j*x0))) for x0 in x])

##
##
fig = plt.figure()
plt.plot(x,yreal,x,yimag)
plt.plot(x,zer,linestyle=":",color="darkslategrey")
#ax.contour3D(X, Y, Z, 50, cmap='binary')

#ax.zaxis.set_rotate_label(False)  # disable automatic rotation
#ax.set_zlabel('$|\Gamma(x+iy)|$',rotation=-90)
##ax.zaxis.set_rotate_label(30) 
#
#
#
#ax.set_zlim3d(0,17.5)
#ax.view_init(10, 10)

plt.xlabel("t")
plt.ylabel(r'$\zeta(\frac{1}{2}+it)$')

plt.show()
##print(complex(x,y))

