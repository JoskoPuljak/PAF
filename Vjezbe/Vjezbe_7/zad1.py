y#moduli
import projectile as proj
import matplotlib.pyplot as plt

#objekt
My_projectile=proj.Projectile(30,55,0.6,0.1,0.02,4)
#grafovi s promjenjivim dt-om
My_projectile.range(0.01)
My_projectile.plot_trajectory("Blue")
My_projectile.reset()

My_projectile.range(0.05)
My_projectile.plot_trajectory("Orange")
My_projectile.reset()

My_projectile.range(0.1)
My_projectile.plot_trajectory("Red")
My_projectile.reset()

My_projectile.range(0.5)
My_projectile.plot_trajectory("Green")
My_projectile.reset()

My_projectile.range(0.2)
My_projectile.plot_trajectory("Purple")
My_projectile.reset()

plt.xlabel("x/m")
plt.ylabel("y/m")
plt.title("ovisnost točnosti x-y grafa o odabranom dt-u za kosi hitac s otporom zraka")
plt.legend([0.01,0.05,0.1,0.5,0.2])
plt.show()
#vidimo za dt otprilike 0.1 metoda daje otprilike precizno rješenje to jest fizikalno rješenje jer y ne pada ispod nule (bar približno)