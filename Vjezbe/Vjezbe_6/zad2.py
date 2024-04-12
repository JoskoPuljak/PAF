import numpy as np
import harmonic_oscillator as harm
My_oscillator=harm.HarmonicOscillator(10,0.1,0,0.3)
Analyitic_period=2*np.pi*np.sqrt(0.1/10)
print(Analyitic_period)
Num_period=My_oscillator.period(0.001)
print(Num_period)
for i in np.arange ()