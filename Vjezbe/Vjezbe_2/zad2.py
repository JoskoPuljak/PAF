#moduli
import matplotlib.pyplot as plt
import math as mt
import numpy as np

#pocetni uvijeti
def kosi_hitac(v0,theta):
    #vrijeme
    dt=0.1
    t=[i*dt for i in range (0,101)]
    #akceleracija
    ax=0
    ay=9.81
    #brzina
    vx=[v0*mt.cos(theta) for i in range(0,101)]
    dvy=ay*dt
    vy=[v0*mt.sin(theta)-dvy*i for i in range(0,101)]   
    #put
    dx=v0*mt.cos(theta)*dt 
    x=[dx*i for i in range (0,101)]
   
    dy=[i*dt for i in vy]
    y=[]
    s=0

    for i in dy:
        y.append(s)
        s+=i
    print(y)
    #y/x graf
    plt.subplot(1,3,1)
    plt.plot(x,y, "r")
    plt.xlabel("x/m")
    plt.ylabel("y/m")
    plt.title("y/x graf")
    plt.subplot(1,3,2)
    #x/t graf
    plt.plot(t,x, "b")
    plt.xlabel("t/s")
    plt.ylabel("x/m")
    plt.title("x/t graf")
    plt.subplot(1,3,3)
    #y/t graf
    plt.plot(t,y,"purple")
    plt.xlabel("t/s")
    plt.ylabel("y/m")
    plt.title("y/t graf")
    print()
    plt.show()
kosi_hitac(50,np.radians(40))

