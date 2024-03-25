import numpy as np
import matplotlib.pyplot as plt
import calculus as clc

#sinus
plt.subplot(1,3,1)
plt.scatter(clc.derivacija(np.sin,0,6,0.01)[0],clc.derivacija(np.sin,0,6,0.01)[1],color="Blue",s=10)
plt.scatter(clc.derivacija(np.sin,0,6,0.1)[0],clc.derivacija(np.sin,0,6,0.1)[1],color="green",s=30)
plt.plot(clc.derivacija(np.sin,0,6,0.01)[0],np.array([np.cos(i) for i in clc.derivacija(np.sin,0,6,0.01)[0]]),color="r")
plt.xlabel("x")
plt.ylabel("sin'(x)")
plt.legend(["$\epsilon$ = 0.01","$\epsilon$ = 0.1","cos(x)-analitičko"])
plt.title("Graf derivacije sinus funkcije")
#kosinus
plt.subplot(1,3,2)
plt.scatter(clc.derivacija(np.cos,0,6,0.01)[0],clc.derivacija(np.cos,0,6,0.01)[1],color="Blue",s=10)
plt.scatter(clc.derivacija(np.cos,0,6,0.1)[0],clc.derivacija(np.cos,0,6,0.1)[1],color="green",s=30)
plt.plot(clc.derivacija(np.cos,0,6,0.01)[0],np.array([-np.sin(i) for i in clc.derivacija(np.sin,0,6,0.01)[0]]),color="r")
plt.xlabel("x")
plt.ylabel("cos'(x)")
plt.legend(["$\epsilon$ = 0.01","$\epsilon$ = 0.1","-sin(x)-analitičko"])
plt.title("Graf derivacije kosinus funkcije")
#kubna
plt.subplot(1,3,3)
plt.scatter(clc.derivacija(lambda a:a**3 ,-6,6,0.01)[0],clc.derivacija(lambda a:a**3,-6,6,0.01)[1],color="Blue",s=10)
plt.scatter(clc.derivacija(lambda a:a**3,-6,6,0.1)[0],clc.derivacija(lambda a:a**3,-6,6,0.1)[1],color="green",s=30)
plt.plot(clc.derivacija(lambda a:a**3,-6,6,0.01)[0],np.array([3*i**2 for i in clc.derivacija(lambda a:a**3,-6,6,0.01)[0]]),color="r")
plt.xlabel("x")
plt.ylabel("(x^3)'")
plt.legend(["$\epsilon$ = 0.01","$\epsilon$ = 0.1","3x^2-analitičko"])
plt.title("Graf derivacije kubne funkcije")
plt.show()