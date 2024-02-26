import matplotlib as plt
import numpy as np
v0=0
s0=0
F=10
m=2
t=np.linspace(0,10,100)
a=F/m

deltav=a*0.1
v=np.array([i*deltav for i in range (0,101)])
deltas=v*0.1
slista=[]
svrijednost=s0
for i in deltas:
    svrijednost+=i
    slista.append(svrijednost)
s=np.array(slista)

plt.plot(a,t)
plt.plot(v,t)
plt.plot(s,t)
plt.show()
