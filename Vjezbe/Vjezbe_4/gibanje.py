import particle as prt
import numpy as np
partic=prt.Particle(5,45,0,0)
time=(2*5*np.sin(np.radians(45)))/9.81
Domet=5*np.cos(np.radians(45))*time
print("Analitički izračunat domet je",Domet)
print("Numerički izračunat domet je",partic.range(0.1))
razlika=Domet-partic.range(0.1)
print("Razlika je", razlika)

#za dt od 0.1s , odstupanje u dometu je 0.074 m
