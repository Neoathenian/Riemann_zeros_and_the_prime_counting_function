

from math import pi
from mpmath import zeta,gamma
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.type_check import imag, real

def xi(z):
    return zeta(z)*0.5*z*(z-1)*pi**(-z/2)*gamma(z/2)


n=100000
x = np.linspace(0,100,n)
zer=np.zeros(n)


y=np.array([float(abs(xi(1/2+1j*x0))) for x0 in x])
yimag=np.array([float(imag(xi(1/2+1j*x0))) for x0 in x])

##
##
print("hola")
fig = plt.figure()
plt.plot(x,yimag)
plt.plot(x,zer,linestyle=":",color="darkslategrey")


plt.xlabel("t")
plt.ylabel(r'$\zeta(\frac{1}{2}+it)$')

plt.show()

