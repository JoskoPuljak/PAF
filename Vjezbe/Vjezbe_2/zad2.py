#moduli
import matplotlib.pyplot as plt
import math as mt

#početni uvijeti
def zad2(v0,theta):
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

    plt.plot(t,vy)
    plt.show()
zad2(5,30)

