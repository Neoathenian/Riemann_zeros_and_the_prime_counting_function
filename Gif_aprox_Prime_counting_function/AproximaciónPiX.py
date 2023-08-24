"""The goal of this script is to create the images for the gif containing:
    1) Prime counting function
    2) Approximation of the prime counting function using the zeros of the Riemann zeta function (with differing amounts of ceros)
    3) Li(x) (is also an approximation of the prime counting function)
    4) x/log(x) (is also an approximation of the prime counting function)
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.integrate import quad
from numpy import log
from sympy import sieve,primepi
from mpmath import li,re
from scipy.special import expi

import os

os.chdir(r"C:\Users\Rafa\Desktop\Python_projects\Riemann_zeros\ImagenesPresentación")

def Integrando(x):
    return 1/x/(x**2-1)/log(x)

def Integral(z):
    integral=quad(Integrando,z,np.inf)
    if integral[1]/integral[0]>0.01:
        print("ERRRORRRRRR",integral[1]/integral[0],flush=True)
    return integral[0]


def J(x,zeros):
    """I don´t know how I got this but I´m pretty sure the Integral was eliminitade for not affecting much idk XD"""
    return float(li(x))-np.sum([re(expi((0.5+cero*1j)*log(x))+expi((0.5-cero*1j)*log(x))) for cero in zeros])#+Integral(x)-log(2)

def J2(x,zeros):
    """Don´t know why I need this, this feels like the original formula, but I´m using the other J(x) (there´s probably an equivalance or something)"""
    return float(li(x))-log(2)-np.sum([li(x**(0.5+cero*1j))+li(x**(0.5-cero*1j)) for cero in zeros])+Integral(x)



def piXaprox(x,n=100,zeros=[]):
    """Riemann formula for the prime counting function"""
    mu=np.array([i for i in sieve.mobiusrange(1,n)])
    return np.sum([mu[i-1]*J(x**(1/i),zeros)/i for i in range(1,n)])

def GraficaPi(N_ceros):
    fig=plt.figure(num=1,clear=True)
    ax=fig.add_subplot(1,1,1)
    x=np.arange(2,1000,0.25)
    pi_teor=[primepi(xi) for xi in x]
    pi_li=[li(xi) for xi in x]
    pi_asint=[xi/log(xi) for xi in x]

    n_suma=100 #This is the number of terms in the sum (which isn´t related to the number of zeros)
    pi_num=[piXaprox(xi,n=n_suma,zeros=ceros[:N_ceros]) for xi in x]
    p1, =plt.plot(x,pi_teor,color="royalblue")
    p2, =plt.plot(x,pi_num,color="orange")
    p3, =plt.plot(x,pi_li,color="green")
    p4, =plt.plot(x,pi_asint,color="red")

    plt.legend([p1,p2,p3,p4],[r"$\pi(x)$",r"$\pi_{aprox}(x)$","li(x)",r"$\frac{x}{\log(x)}$"])
    plt.title(f"nºceros={N_ceros}")
    plt.savefig(f"AproxPi/N_ceros={N_ceros}_n={n_suma}.png")
    #plt.show(block=False)



os.makedirs("AproxPi",exist_ok=True)

ceros=np.loadtxt("ZerosZetaRiemann2M.txt",skiprows=1,max_rows=10000)
print(np.sum(ceros<50))

for i in range(0,100):
    GraficaPi(i)
    #plt.show()