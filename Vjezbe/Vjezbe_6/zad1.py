#moduli
import harmonic_oscillator as harm
import matplotlib.pyplot as plt
import numpy as np
#Vrijednost

My_oscillator=harm.HarmonicOscillator(10,0.1,0,0.3)
My_oscillator.oscillate(2,0.01)
My_oscillator.plot_trajectory()
My_oscillator.reset()
plt.show()

#Preciznost
#Korak 0.05
My_oscillator.oscillate(2,0.05)
My_oscillator.plot_x("purple")
My_oscillator.reset()

#Korak 0.01
My_oscillator.oscillate(2,0.01)
My_oscillator.plot_x("red")
My_oscillator.reset()

#Korak 0.001
My_oscillator.oscillate(2,0.001)
My_oscillator.plot_x("blue",20)
#Analytic
Analytic=[0.3*np.cos(np.sqrt(10/0.1)*t) for t in My_oscillator.t]
plt.plot(My_oscillator.t,Analytic, color="black", linewidth="3")
My_oscillator.reset()

plt.legend(["dt=0.05","dt=0.01","dt=0.001","Analytic"])
plt.show()