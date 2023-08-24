from mpmath import *
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.type_check import imag, real



n=1000
x = np.linspace(0,0.9,n)
zer=np.zeros(n)

yreal=np.array([float(real(zeta(x0))) for x0 in x])
yimag=np.array([float(imag(zeta(x0))) for x0 in x])

plt.plot(x,yreal,x,zer)
#plt.plot(x,yimag)

plt.show()