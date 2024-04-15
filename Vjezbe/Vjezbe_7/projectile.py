import numpy as np
import matplotlib.pyplot as plt
def sgn(number):
    if number<=0:
        return(-1)
    else:
        return(1)

class Projectile:
    def __init__(self,v_0,kut,rho,Cd,A,m):
        g=9.81
        self.constant=(rho*Cd*A)/(2*m)
        self.x=[0]
        self.y=[0]
        self.vx=[v_0*np.cos(np.radians(kut))]
        self.vy=[v_0*np.sin(np.radians(kut))]
        self.kut=kut
        self.t=[0]
        self.ax=[-1*sgn(self.vx[0])*self.constant*self.vx[0]**2]
        self.ay=[-g-(-1*sgn(self.vy[0])*self.constant*self.vy[0]**2)]
    def reset(self):
        self.ax=[self.ax[0]]
        self.ay=[self.ay[0]]
        self.vx=[self.vx[0]]
        self.vy=[self.vy[0]]
        self.x=[self.x[0]]
        self.y=[self.y[0]]
        self.t=[0]
    def __move(self,dt):
        g=9.81
        self.t.append(self.t[-1] +dt)
        self.vx.append(self.vx[-1]+self.ax[-1]*dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*dt)
        self.x.append(self.x[-1]+self.vx[-1]*dt)
        self.y.append(self.y[-1]+self.vy[-1]*dt)
        self.ax.append(-1*sgn(self.vx[-1])*self.constant*self.vx[-1]**2)
        self.ay.append(-g-(-1*sgn(self.vy[-1])*self.constant*self.vy[-1]**2))

    
        
    def range(self,dt):
        while self.y[-1]>=0:
            self.__move(dt)
            
        domet=self.x[-1]
        return domet
    def plot_trajectory(self,colour="Red"):
        plt.plot(self.x,self.y, color=colour)
        plt.xlabel("x/m")
        plt.ylabel("y/m")
        plt.title("x/y graf")
        
    
