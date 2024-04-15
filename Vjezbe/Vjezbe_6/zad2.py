#moduli
import numpy as np
import harmonic_oscillator as harm
import matplotlib.pyplot as plt
#definiranje objekta
My_oscillator=harm.HarmonicOscillator(10,0.1,0,0.3)
#racunanje reltativne pogreske za dt od 0.0001 do 0.1
dt=np.arange(0.0001,0.1,0.0001)
Analyitic_period=2*np.pi*np.sqrt(0.1/10)
lista_rel_pogreske=[]
for i in dt:
    Num_period=My_oscillator.period(i)
    My_oscillator.reset()
    rel_pogreska=(abs(Analyitic_period-Num_period)/Analyitic_period)*100
    lista_rel_pogreske.append(rel_pogreska)

#plotanje grafa pogreske
plt.plot(dt,lista_rel_pogreske,color="green")
plt.xlabel("dt/s")
plt.ylabel("relativna pogreska u %")
plt.title("Ovisnost pogreske o dt-u")
plt.show()
#što je veći dt, veća je pogreska
