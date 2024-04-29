import elektromag as elek
import matplotlib.pyplot as plt

#definicije objekta
Elektron=elek.elektromag([0,0,0],[0,0,1],[0.1,0.1,0.1],1,-1)
Proton=elek.elektromag([0,0,0],[0,0,1],[0.1,0.1,0.1],1,1)

#plotanje Euler
fig=plt.figure()
ax=plt.axes(projection="3d")
Et_euler=Elektron.trajectory(0.01,20)
ax.plot(Et_euler[0],Et_euler[1],Et_euler[2],color="yellow")
Pt_euler=Proton.trajectory(0.01,20)
ax.plot(Pt_euler[0],Pt_euler[1],Pt_euler[2],color="red")
Elektron.reset()
Proton.reset()

#Plotanje Runge_Kutta
Et_runge=Elektron.Runge_trajectory(0.01,20)
ax.plot(Et_runge[0],Et_runge[1],Et_runge[2],color="yellow",linestyle="--")
Pt_runge=Proton.Runge_trajectory(0.01,20)
ax.plot(Pt_runge[0],Pt_runge[1],Pt_runge[2],color="red",linestyle="--")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.legend(["Elektron Euler","Proton Euler","Elektron Runge","Proton Runge"])
plt.show()
#resetanje
Elektron.reset()
Proton.reset()