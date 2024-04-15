import projectile as proj
import matplotlib.pyplot as plt
My_projectile=proj.Projectile(30,55,0.6,0.1,0.02,4)

My_projectile.range(0.01)
My_projectile.plot_trajectory("Blue")
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
plt.show()
