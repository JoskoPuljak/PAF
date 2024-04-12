#moduli
import numpy as np
import matplotlib.pyplot as plt
#klasa
class HarmonicOscillator:
    #početni uvjeti
    def __init__(self,k,m,v0,x0):
        self.k=k
        self.m=m
        self.t=[0]
        self.x=[x0]
        self.v=[v0]
        self.a=[-self.k/self.m*x0]
    #resetiranje lista
    def reset(self):
        self.t=[self.t[0]]
        self.x=[self.x[0]]
        self.v=[self.v[0]]
        self.a=[self.a[0]]
    #punjenje lista
    def oscillate(self,t,dt):
        for i in np.arange(0,t,dt):
            self.t.append(self.t[-1]+dt)
            self.a.append(-self.k/self.m*self.x[-1])
            self.v.append(self.v[-1]+(self.a[-1]*dt))
            self.x.append(self.x[-1]+(self.v[-1]*dt))
            
    #crtanje        
    def plot_trajectory(self):
        plt.subplot(1,3,1)
        plt.plot(self.t,self.x,color="blue")
        plt.subplot(1,3,2)
        plt.plot(self.t,self.v,color="green")
        plt.subplot(1,3,3)
        plt.plot(self.t,self.a,color="purple")
        plt.show()
    def plot_x(self,colour,size=30):
        plt.scatter(self.t,self.x,color=colour,s=size)







