import elektromag as elek
import matplotlib.pyplot as plt

#definicije objekta
Elektron=elek.elektromag([0,0,0],[0,0,1],[0.1,0.1,0.1],1,-1)
Proton=elek.elektromag([0,0,0],[0,0,1],[0.1,0.1,0.1],1,1)

#plotanje
fig=plt.figure()
ax=plt.axes(projection="3d")
Et=Elektron.trajectory(0.01,20)
ax.plot(Et[0],Et[1],Et[2],color="yellow")
Pt=Proton.trajectory(0.01,20)
ax.plot(Pt[0],Pt[1],Pt[2],color="red")

plt.show()
#resetanje
Elektron.reset()
Proton.reset()