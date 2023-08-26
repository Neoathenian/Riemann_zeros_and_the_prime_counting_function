from cmath import pi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def f(deltas,alpha,beta,epsilon):
    contador=0
    N=10**6
    for i in range(N):
        j=0
        suma=0
        while suma<beta:
            suma+=deltas[i+j]
            j+=1
            if alpha<=suma<beta:
                contador+=1 
    return contador/N/epsilon

def g(x):
    return 1-(np.sin(pi*x)/(pi*x))**2


Zeros=pd.read_table("ZerosZetaRiemann2M.txt")
Zeros["Index"]=Zeros.index

#Calculemos los deltas
H=np.insert(np.array(Zeros["Ceros Zeta de Riemann"][:-1]),0,1)#El primer elemento lo eliminaremos, pero de momento empujamos todo el vector poniendo un 1 al principio
Zeros["Delta"]=(Zeros["Ceros Zeta de Riemann"]-H)*(np.log(H/2/pi))/(2*pi)
Zeros=Zeros[1:]


#Calculemos los valores de la densidad
epsilon=0.01
x=np.arange(epsilon,3+epsilon,epsilon)#Nos saltamos el 0 porque dividiríamospor 0
y=np.array([f(np.array(Zeros["Delta"]),x[i],x[i+1],epsilon) for i in range(len(x)-1)])

#Plot Densidad Montgomery/Odlyzko
plt.plot(x[:-1],y,".",x[:-1],g(x[:-1]))
plt.xlabel("x")
plt.legend([r"$\frac{1}{N\epsilon}|\{(n,k):1\leq n\leq N,\delta_n+\dots\delta_{n+k}\in[x,x+\epsilon]\}|$",r"$1-\left(\frac{\sin(\pi x)}{\pi x}\right)^2$"])
#plt.legend([r"$1-\Big(\frac{\sin(\pi x)}{\pi x}\Big)^2$",r"$\frac{1}{N\epsilon}|\{(n,k):1\leq n\leq N,\delta_n+\dots\delta_{n+k}\in[x,x+\epsilon]\}|$"])
plt.show()
