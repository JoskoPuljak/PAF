import calculus as clc
import numpy as np
import matplotlib.pyplot as plt
#funkcija je 2x^2+3
raspon=range(10,50)
Prav_donja=[clc.pravokutna_integracija(lambda a:2*a**2+3,0,1,i)[0] for i in raspon] 
Prav_gornja=[clc.pravokutna_integracija(lambda a:2*a**2+3,0,1,i)[1] for i in raspon]
Trap=[clc.trapezna_integracija(lambda a:2*a**2+3,0,1,i) for i in raspon]
#analiticki
Analiticko=(2/3)*1**3+3*1
Analitic_list=[Analiticko for i in raspon] 

#grafovi
plt.scatter(list(raspon),Prav_donja,color="blue")
plt.scatter(list(raspon),Prav_gornja,color="red")
plt.scatter(list(raspon),Trap,color="purple")
plt.plot(list(raspon),Analitic_list,color="orange")
plt.xlabel("broj koraka")
plt.ylabel("vrijednost integrala")
plt.title("graf vrijednosti integrala u ovisnosti o broju koraka")
plt.legend(["Donja meda pravokutne integracije","Gornja međa pravokutne integracije","Trapezna interacija","Analiticko izračunata vrijednost"])
plt.show()