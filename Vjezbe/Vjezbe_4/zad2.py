#moduli
import particle as prt
import numpy as np
import matplotlib.pyplot as plt
#definicija cestice
p1=prt.Particle(10,60,0,0)

#racunanje analitickog
time=(10*2*np.sin(np.radians(60)))/9.81
D_analiticki=10*np.cos(np.radians(60))*time

#funkcija relativne pogreske
def relativna_pogreska(dt):
    rel_pogreska=((abs(D_analiticki-p1.range(dt)))/D_analiticki)*100
    p1.reset()
    return rel_pogreska

#polja
t=[i*0.0001 for i in range(1,1001)]
pogreska=[relativna_pogreska(i*0.0001) for i in range(1,1001)]

#graf
plt.plot(t,pogreska,color="purple")
plt.xlabel("dt/s")
plt.ylabel("pogreška u %")
plt.title("Ovisnost pogreske o dt-u")
plt.show()
