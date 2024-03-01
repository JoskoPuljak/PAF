#moduli
import matplotlib.pyplot as plt
import numpy as np
#pocetni uvijeti
F=int(input("Upiši silu u Njutnima"))
m=int(input("Upiši masu u kilogramima"))
#a/t graf
t=np.linspace(0,10,100)
a_val=F/m
a=np.array([a_val for i in t])
plt.subplot(3,1,1)
plt.ylabel("a/m/s^2")
plt.title("a/t graf")
plt.plot(t,a,color="purple")
#v/t graf
v=a_val*t
plt.subplot(3,1,2)
plt.ylabel("v/m/s")
plt.title("v/t graf")
plt.plot(t,v,color="pink")
#x/t graf
x=np.array([(i*(j**2))/2 for i,j in zip(a,t)])
plt.subplot(3,1,3)
plt.plot(t,x,color="blue")
plt.ylabel("x/m")
plt.xlabel("t/s")
plt.title("x/t graf")
plt.show()