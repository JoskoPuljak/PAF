#moduli
import matplotlib.pyplot as plt
import numpy as np
#pocetni uvijeti
F=int(input("Upisi silu u Njutnima"))
m=int(input("Upisi masu u kilogramima"))
#a/t graf
t=np.linspace(0,10,100)
a_val=F/m
a=np.array([a_val for i in t])
plt.subplot(3,1,1)
plt.ylabel("a/m/s^2")
plt.title("a/t graf")
plt.plot(t,a,color="purple")
#v/t graf
dt=0.1
dv=a*dt
v=[dv*i for i in range(0,100)]

print(v)
plt.subplot(3,1,2)
plt.ylabel("v/m/s")
plt.title("v/t graf")
plt.plot(t,v,color="pink")
#x/t graf

plt.subplot(3,1,3)
plt.plot(t,x,color="blue")
plt.ylabel("x/m")
plt.xlabel("t/s")
plt.title("x/t graf")
plt.show()