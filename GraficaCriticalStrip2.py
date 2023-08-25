"""This script is to get an image of the critical strip with a bunch of zeros zoomed out for my presentation"""
import matplotlib.pyplot as plt
import numpy as np

import os
os.chdir(r"C:\Users\Rafa\Desktop\Python_projects\Riemann_zeros\ImagenesPresentación")


ceros=np.loadtxt("ZerosZetaRiemann2M.txt",skiprows=1,max_rows=10000)
x_ceros=np.zeros(len(ceros))+0.5

n=1000
y_max=500

MuchosCeros=np.zeros(n)
x=np.linspace(-y_max,y_max,n)

EjeX=np.linspace(-100,100,n)

fig, ax = plt.subplots()
#fig =plt.figure
#ax.plot(MuchosCeros,x,"--",color="black")
#ax.plot(MuchosCeros+1,x,"--",color="black")
p1, =ax.plot(MuchosCeros+0.5,x,"--",color="red")
ax.plot(EjeX,MuchosCeros,color="black",linewidth=0.5)


p2, =ax.plot(x_ceros,ceros,".",color="black",markersize=1)
ax.plot(x_ceros,-ceros,".",color="black",markersize=1)
ax.plot(np.arange(-100,0,2),np.zeros(50),"o",color="black")

p3=ax.fill_between(np.linspace(0,1,n),MuchosCeros-y_max,MuchosCeros+y_max, facecolor="lightskyblue",alpha=0.4)

plt.ylim([-y_max,y_max])
plt.xlim([-0.5,1.5])
plt.legend([p2,p3,p1],[r"Ceros $\zeta(z)$","Banda Crítica","Línea Crítica"])
#plt.legend([p3,p2],["Banda Crítica","Línea Crítica"])

#plt.xticks(np.arange(-2,3+1,1))

#ax.axes.get_yaxis().set_visible(False)
plt.show()
