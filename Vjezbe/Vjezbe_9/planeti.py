import numpy as np
import matplotlib.pyplot as plt
class dvaplaneta:
    def __init__ (self,x_Sunce,x_Zemlja,v0_Zemlja):
        self.G=6.67408*(10**(-11))
        self.Ms=1.989*(10**30)
        self.Mz=5.9742*(10**24)
        self.x_Sunce=[np.array(x_Sunce)]
        self.x_Zemlja=[np.array(x_Zemlja)]
        self.v_Zemlja=[np.array((0,v0_Zemlja))]
        self.v_Sunce=[np.array((0,0))]
        self.a_Sunce=[np.array(((-self.G*(self.Ms)/abs(self.x_Sunce[0][0]-self.x_Zemlja[0][0])**3)*(self.x_Sunce[0][0]-self.x_Zemlja[0][0]),(-self.G*(self.Ms)/abs(self.x_Sunce[0][1]-self.x_Zemlja[0][1])**3)*(self.x_Sunce[0][1]-self.x_Zemlja[0][1])))]
        self.a_Zemlja=[np.array(((-self.G*(self.Mz)/abs(self.x_Zemlja[0][0]-self.x_Sunce[0][0])**3)*(self.x_Zemlja[0][0]-self.x_Sunce[0][0]),(-self.G*(self.Mz)/abs(self.x_Zemlja[0][1]-self.x_Sunce[0][1])**3)*(self.x_Zemlja[0][1]-self.x_Sunce[0][1])))]
    def reset(self):
        self.x_Sunce=[self.x_Sunce[0]]
        self.x_Zemlja=[self.x_Zemlja[0]]
        self.v0_Zemlja=[self.v_Zemlja[0]]
        self.v_Sunce=[self.v_Sunce[0]]
        self.a_Sunce=[self.a_Sunce[0]]
        self.a_Zemlja=[self.a_Zemlja[0]]
    def __move(self,dt):
        self.v_Sunce.append(np.array(self.v_Sunce[-1][0]+self.a_Sunce[-1][0]*dt,self.v_Sunce[-1][1]+self.a_Sunce[-1][1]*dt))
        self.v_Zemlja.append(np.array(self.v_Zemlja[-1][0]+self.a_Zemlja[-1][0]*dt,self.v_Zemlja[-1][1]+self.a_Zemlja[-1][1]*dt))
        self.x_Sunce.append(np.array(self.x_Sunce[-1][0]+self.v_Sunce[-1][0]*dt,self.x_Sunce[-1][1]+self.v_Sunce[-1][1]*dt))
        self.x_Zemlja.append(np.array(self.x_Zemlja[-1][0]+self.v_Zemlja[-1][0]*dt,self.x_Zemlja[-1][1]+self.v_Zemlja[-1][1]*dt))
        self.a_Sunce.append(np.array(((-self.G*(self.Ms)/abs(self.x_Sunce[-1][0]-self.x_Zemlja[-1][0])**3)*(self.x_Sunce[-1][0]-self.x_Zemlja[-1][0]),(-self.G*(self.Ms)/abs(self.x_Sunce[-1][1]-self.x_Zemlja[-1][1])**3)*(self.x_Sunce[-1][1]-self.x_Zemlja[-1][1]))))
        self.a_Zemlja.append((((-self.G*(self.Mz)/abs(self.x_Zemlja[-1][0]-self.x_Sunce[-1][0])**3)*(self.x_Zemlja[-1][0]-self.x_Sunce[-1][0]),(-self.G*(self.Mz)/abs(self.x_Zemlja[-1][1]-self.x_Sunce[-1][1])**3)*(self.x_Zemlja[-1][1]-self.x_Sunce[-1][1]))))
    def plot_trajectory(self,dt,t):
        for i in np.arange(0,t,dt):
            self.__move(dt)
        xs=self.x_Sunce[0]
        ys=self.x_Sunce[1]
        xz=self.x_Zemlja[0]
        yz=self.x_Zemlja[1]
        plt.plot(xs,ys,color="yellow")
        plt.plot(xz,yz,color="blue")
        plt.show()
Sunceizemlja=dvaplaneta((0,0),(0,1.486*10**11),29783)
Sunceizemlja.plot_trajectory(10,31556909)