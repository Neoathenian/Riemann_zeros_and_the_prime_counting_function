import numpy as np
from numpy import pi
import matplotlib.pyplot as plt


def T(beta,psi):
    return beta+np.pi-2*psi

def cc(beta):
    return np.cos(beta),np.sin(beta)

#Se puede ver como el número de movimientos que hace por la circunferencia
def N_choques(beta,psi,epsilon):
    contador=0
    while abs(beta)>epsilon/2:#Mientras no golpee el agujero
        contador+=1
        beta=T(beta,psi)
        beta=(beta+pi)%(2*pi)-pi
    return contador

def Tiempo_Escape(beta,psi,epsilon):
    return N_choques(beta,psi,epsilon)*2*np.cos(psi)

#Uso el append method que creo que es lento, pero el objetivo no es usar esta función apenas así que no debería importar
def Recorrido(beta,psi,epsilon):
    contador=0
    B=[]
    B.append(beta)
    while abs(beta)>epsilon/2:#Mientras no golpee el agujero
        contador+=1
        beta=T(beta,psi)
        beta=(beta+pi)%(2*pi)-pi
        B.append(beta)
    return B

#Usa como variable una sucesion de betas
def Plot_Recorrido(B):
    X=cc(B)
    plt.plot(X[0],X[1],"green")

def Plot_Circunferencia(epsilon):
    #Esto nos dibuja el círculo
    Circ=cc(np.linspace(epsilon/2,2*pi-epsilon/2,100))
    plt.plot(Circ[0],Circ[1],"blue")
    Agujero=cc(np.linspace(-epsilon/2,epsilon/2,10))
    plt.plot(Agujero[0],Agujero[1],"red")


#parametros iniciales
epsilon=0.001
n=10**7


beta=np.random.uniform(-pi,pi,n)
#psi=np.arcsin(np.random.uniform(-1,1,n))#Esto es para seguir la distribución dada por el paper(que no es la uniforme sino cos(psi)/2dpsi)
psi=np.random.uniform(-pi/2,pi/2,n)

N=np.array([Tiempo_Escape(beta[i],psi[i],epsilon) for i in range(len(beta))])


def P1(t,N):
    return np.array([np.sum(N>s)/len(N) for s in t])

t=np.linspace(n/50,10*n,10)

#plt.plot(t,P1(t,N)*100)
print(2/epsilon)
plt.plot(t,P1(t,N)*t)
plt.xlabel("t")
plt.ylabel(f"P1(t,N)*t-2/epsilon con epsilon={epsilon}")
plt.show()
#print((t*P1-2/epsilon))

plt.plot(t,P1(t,N))
plt.xlabel("t")
plt.ylabel(f"P1(t,N)")
plt.show()



#beta=np.random.uniform(-pi,pi,1)
#psi=np.arcsin(np.random.uniform(-1,1,1))#Esto es para seguir la distribución dada por el paper(que no es la uniforme sino cos(psi)/2dpsi)
#
#Plot_Recorrido(Recorrido(beta,psi,epsilon))
#Plot_Circunferencia(epsilon)
#
##print(len(Recorrido(beta,psi,epsilon)))
##print(N_choques(beta,psi,epsilon))
#
#
#plt.show()
#


#print(epsilon**(alpha-0.5)*(t*P1-2/epsilon))

#print(N_choques(beta,psi,epsilon))
#
#Plot_Circunferencia()
#Plot_Recorrido(Recorrido(beta,psi,epsilon))
#
#plt.show()



