"""This creates files to be used in BillarTiemposLectorArchivos.py BE CAREFUL AS IT IS USING A WHILE TRUE as the more data the better lmao"""
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import os

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


def P1(t,N):
    return np.array([np.sum(N>s)/len(N) for s in t])



def CrearDatos(epsilon=0.01):
    dir=f"BillarDistribuidosUnif[-pi,-pi]xasin([-pi2,pi2])/epsilon={epsilon}"
    if not os.path.exists(dir):
        os.makedirs(dir)

    inic=len(os.listdir(dir))
    n=10**5
    while True:
        psi=np.arcsin(np.random.uniform(-1,1,n))#Esto es para seguir la distribución dada por el paper(que no es la uniforme sino cos(psi)/2dpsi)
        beta=np.random.uniform(-pi,pi,n)
        
        Escritura=np.array([beta,psi,[Tiempo_Escape(beta[i],psi[i],epsilon) for i in range(len(beta))]])
        filename=dir+f"/num_{inic}"
        np.save(filename,Escritura)
        inic+=1
        print("Se ha escrito exitosamente en",filename,flush=True)


CrearDatos(epsilon=0.05)

###Esto sirve para comprobar que las distribuciones son las esperadas,
##A=np.load("NUEVOTXT2.npy")
##plt.hist(A[0])
##plt.show()
##plt.hist(A[1])
##plt.show()
