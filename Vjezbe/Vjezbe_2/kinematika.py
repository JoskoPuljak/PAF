#moduli
import matplotlib.pyplot as plt
import numpy as np
#pocetni uvijeti
def jednoliko_gibanje(F,m):
    #a/t graf
    a_val=F/m
    dt=0.1
    t=[0.1*i for i in range (0,101)]
    a=[a_val for i in range(0,101)]
    plt.subplot(3,1,1)
    plt.ylabel("a/m/s^2")
    plt.title("a/t graf")
    plt.plot(t,a,color="purple")
    #v/t graf
    dv=a_val*dt
    v=[dv*i for i in range (0,101)]
    plt.subplot(3,1,2)
    plt.ylabel("v/m/s")
    plt.title("v/t graf")
    plt.plot(t,v,color="pink")
    #x/t graf
    dx=[i*dt for i in v]
    x=[]
    sum=0
    for i in dx:
        sum+=i
        x.append(sum)
    plt.subplot(3,1,3)
    plt.plot(t,x,color="blue")
    plt.ylabel("x/m")
    plt.xlabel("t/s")
    plt.title("x/t graf")
    plt.show()



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
    plt.show()


