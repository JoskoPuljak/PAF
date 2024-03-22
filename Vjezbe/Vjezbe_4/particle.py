import numpy as np
import matplotlib.pyplot as plt
class Particle:
    def __init__(self,v_0,kut,x_0,y_0):
        self.vx=v_0*np.cos(np.radians(kut))
        self.vy=[v_0*np.sin(np.radians(kut))]
        self.kut=kut
        self.x=[x_0]
        self.y=[y_0]
        self.t=[0]
    def reset(self):
        self.vy=[self.vy[0]]
        self.x=[self.x[0]]
        self.y=[self.y[0]]
        self.t=[0]
    def __move(self,dt):
        g=9.81
        self.t.append(self.t[-1] +dt)
        self.x.append(self.x[-1]+self.vx*dt)
        self.vy.append(self.vy[-1]-g*dt)
        self.y.append(self.y[-1]+self.vy[-1]*dt)
    def range(self,dt):
        while self.y[-1]>=0:
            self.__move(dt)
            
        domet=self.x[-1]
        return domet
    def plot_trajectory(self):
        plt.plot(self.x,self.y, color="red")
        plt.xlabel("x/m")
        plt.ylabel("y/m")
        plt.title("x/y graf")
        plt.show()
        



    


        
