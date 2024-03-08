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

jednoliko_gibanje(20,5)