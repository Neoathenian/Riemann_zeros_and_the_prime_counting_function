"""Used to make MediaDistanciasGeneralizadas.png (Used to check that The mean of the normalized distances between zeros of the Riemann Zeta function -> 1))"""
from cmath import pi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


Zeros=pd.read_table("ZerosZetaRiemann2M.txt")
Zeros["Index"]=Zeros.index

#Calculemos los deltas
H=np.insert(np.array(Zeros["Ceros Zeta de Riemann"][:-1]),0,1)#El primer elemento lo eliminaremos, pero de momento empujamos todo el vector poniendo un 1 al principio
Zeros["Delta"]=(Zeros["Ceros Zeta de Riemann"]-H)*(np.log(H/2/pi))/(2*pi)
Zeros=Zeros[1:]

#Calculamos las medias
Zeros["Media"]=Zeros["Delta"].cumsum()/Zeros["Index"]

#Plot medias
#plt.xlim([-10,500])
plt.xlabel("M")
plt.ylabel(r'$\frac{1}{M}\sum {}_{n=1}^M \delta_n$')
plt.plot(Zeros["Media"][:10**3])
plt.show()