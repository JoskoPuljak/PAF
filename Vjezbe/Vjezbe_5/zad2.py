import calculus as clc
import numpy as np
import matplotlib.pyplot as plt
#funkcija je 2x^2+3
raspon=range(10,50)
Prav_donja=[clc.pravokutna_integracija(lambda a:2*a**2+3,0,1,i)[0] for i in raspon] 
Prav_gornja=[clc.pravokutna_integracija(lambda a:2*a**2+3,0,1,i)[1] for i in raspon]
Prav_trap=[clc.trapezna_integracija(lambda a:2*a**2+3,0,1,i) for i in raspon]

plt.scatter(list(raspon),Prav_donja,color="blue")
plt.scatter(list(raspon),Prav_gornja,color="red")
plt.scatter(list(raspon),Prav_trap,color="purple")
#plt.plot(list(raspon),[(2*a**3)/3+ 3*a for a in ])
plt.show()