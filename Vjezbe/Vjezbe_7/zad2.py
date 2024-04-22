import projectile as proj
import matplotlib.pyplot as plt
My_projectile=proj.Projectile(30,55,0.6,0.1,0.02,4)

#Runge-kutta korak 0.01
My_projectile.Runge_range(0.01)
My_projectile.plot_trajectory("Blue")
My_projectile.reset()

#Euler korak 0.01
My_projectile.range(0.01)
My_projectile.plot_trajectory("Purple")
My_projectile.reset()

#Euler korak 0.05
My_projectile.range(0.05)
My_projectile.plot_trajectory("Green")
My_projectile.reset()

#Euler korak 0.1
My_projectile.range(0.1)
My_projectile.plot_trajectory("Orange")
My_projectile.reset()

#plottanje
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.legend(["Runge_Kutta 0.01","Euler 0.01","Euler 0.05","Euler 0.1"])
plt.show()

#Vidimo da je Runge-kutta metoda preciznija od Euler metode