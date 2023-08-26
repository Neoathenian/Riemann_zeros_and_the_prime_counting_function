"""This script is to obtain the gif from the images created by AproximaciónPiX.py"""
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
#import imageio
import os


def Compilar_Gif():
    path="AproxPi/"
    filenames=os.listdir(path)
    with imageio.get_writer('mygif.gif', mode='I') as writer:
        for j in range(100):
            image = imageio.imread(path+"/"+f"N_ceros={j}_n=100.png")
            print(f"_{j}",flush=True)
            writer.append_data(image)

Compilar_Gif()
