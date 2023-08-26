"""This script alone creates the images and the Gif for the pool table (billiard table)"""
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
#import imageio
import imageio.v2 as imageio
import os

os.makedirs("ImgsBilliardsGif",exist_ok=True)

def T(beta,psi):
    beta= beta+np.pi-2*psi
    return (beta+pi)%(2*pi)-pi

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
        B.append(beta)
    return B

def Interpolar(now,next,n):
    x=np.linspace(now[0],next[0],n)
    y=now[1]+(next[1]-now[1])/(next[0]-now[0])*(x-now[0])
    return x,y

def Gif(beta,psi,epsilon):
    Betas=Recorrido(beta,psi,epsilon)
    ccBetas=cc(Betas)
    k=0
    ntrazas=5
    filenames = []
    for i in range(len(Betas)-1):
        if i<ntrazas:#a partir de que haya cinco empezamos a borrar por detrás
            k=i
        else:
            k=ntrazas
        now=cc(Betas[i])
        next=cc(Betas[i+1])

        n=7        
        x,y=Interpolar(now,next,n)
        
        # create file name and append it to a list
        for j in range(n):
            Plot_Circunferencia(epsilon)

            #Dibujemos el primer trazo (que se va borrando)
            inicx,inicy=Interpolar(cc(Betas[i-k]),cc(Betas[i-k+1]),n)
            if k==ntrazas:
                plt.plot(inicx[j:],inicy[j:],color="green")#Dibujamos la pelotita
            else:
                plt.plot(inicx,inicy,color="green")#Dibujamos la pelotita


            #ploteemos el pasado:
            plt.plot(ccBetas[0][i-k+1:i+1],ccBetas[1][i-k+1:i+1],color="green")#Queremos dibujar hasta el i incluido (dibujamos del pasado k instante anteriores)
            

            plt.plot([now[0],x[j]],[now[1],y[j]],color="green")#Dibujamos hasta la pelotitas
            plt.plot(x[j],y[j],".",markersize=10,color="black")#Dibujamos la pelotita
            


            filename = f'ImgsBilliardsGif/{i}_{j}.png'
            filenames.append(filename)
            plt.savefig(filename)
            plt.close()


        # save frame
        #plt.close()
    # build gif
    with imageio.get_writer('mygif.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
        
    # Remove files
    for filename in set(filenames):
        os.remove(filename)





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
epsilon=0.2
np.random.seed(5)
beta=np.random.uniform(-pi,pi,1)
psi=np.arcsin(np.random.uniform(-1,1,1))#Esto es para seguir la distribución dada por el paper(que no es la uniforme sino cos(psi)/2dpsi)

beta=beta[0]
psi=psi[0]

Gif(beta,psi,epsilon)
