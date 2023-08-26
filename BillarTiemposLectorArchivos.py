"""Used to make the GraficaDistintosTiempos_epsilon=0.05.png, which uses data created from BillarTiemposCreadorArchivos"""
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



def LeerTodosLosDatos(epsilon=0.01,asinunif=True):
    if asinunif:
        dir=f"BillarDistribuidosUnif[-pi,-pi]xasin([-pi2,pi2])/epsilon={epsilon}/"
    else:
        dir=f"BillarDistribuidosUnif[-pi,-pi]x[-pi2,pi2]/epsilon={epsilon}/"
    
    if not os.path.exists(dir):
        return 
    
    filenames=os.listdir(dir)
    anterior=[[],[],[]]
    for filename in filenames:
        a=np.load(dir+filename)
        anterior=np.concatenate((anterior,a),axis=1)
    #comprobador distribuciones
    plt.hist(anterior[0])
    plt.show()
    if asinunif:
        plt.hist(np.sin(anterior[1]))
        plt.show()
    else:
        plt.hist(anterior[1])
        plt.show()

    n=len(anterior)
    #Veamos nuestra funcion
    t=np.linspace(10**5,10*n,1000)
    plt.plot(t,P1(t,anterior[2])*t)
    plt.xlabel("t")
    plt.ylabel(f"P1(t,N)*t")#-2/epsilon con epsilon={epsilon}")
    plt.show()


def LeerDatosEnPartes(epsilon=0.01,asinunif=True):
    if asinunif:
        dir=f"BillarDistribuidosUnif[-pi,-pi]xasin([-pi2,pi2])/epsilon={epsilon}/"
    else:
        dir=f"BillarDistribuidosUnif[-pi,-pi]x[-pi2,pi2]/epsilon={epsilon}/"
    
    if not os.path.exists(dir):
        return 
    
    filenames=os.listdir(dir)
    anterior=[[],[],[]]
    for filename in filenames:
        a=np.load(dir+filename)
        anterior=np.concatenate((anterior,a),axis=1)
    print("datos han sido leidos",flush=True)

    n=len(anterior[2])
    #Veamos nuestra funcion
    t=np.linspace(10**5,n*10,1000)
    print("Cree el vector t",flush=True)
    plt.plot(t,P1(t,anterior[2][:int(n/100)])*t,t,P1(t,anterior[2][:int(n/10)])*t,t,P1(t,anterior[2])*t)
    print("lo mande a plotear",flush=True)
    plt.xlabel("t")
    plt.ylabel(r"$P_1(t,N)\cdot t$")#-2/epsilon con epsilon={epsilon}")
    plt.title(f"epsilon={epsilon}")
    plt.legend([f"{int(n/100):.1e} datos",f"{int(n/10):.1e} datos",f"{n:.1e} datos"])
    print("Preparado para mostrar",flush=True)
    plt.savefig(f"GraficaDistintosTiempos_epsilon={epsilon}.png")
    plt.show()

 
    

LeerDatosEnPartes(epsilon=0.05)

###Esto sirve para comprobar que las distribuciones son las esperadas,
##A=np.load("NUEVOTXT2.npy")
##plt.hist(A[0])
##plt.show()
##plt.hist(A[1])
##plt.show()
