#moduli
import matplotlib.pyplot as plt
import numpy as np
#klasa
class elektromag:
    def __init__(self,E,B,v,m,q):
        self.E=np.array(E)
        self.B=np.array(B)
        self.v=[np.array(v)]
        self.m=m
        self.q=q
        self.a=[(self.q/self.m)*(self.E+np.cross(self.v[-1],self.B))]
        self.x=[np.array([0,0,0])]
    def reset(self):
        self.v=[self.v[0]]
        self.a=[self.a[0]]
        self.x=[self.x[0]]

    def __move(self,dt):
        self.v.append(self.v[-1]+self.a[-1]*dt)
        self.x.append(self.x[-1]+self.v[-1]*dt)
        self.a.append((self.q/self.m)*(self.E+np.cross(self.v[-1],self.B)))
    def trajectory(self,dt,t):
        for i in np.arange(0,t,dt):
            self.__move(dt)
        z=[i[2] for i in self.x]
        y=[i[1] for i in self.x]
        x=[i[0] for i in self.x]
        return x,y,z
    def __Rungemove(self,dt):
        k1v=self.a[-1]*dt
        k2v=(self.q/self.m)*(self.E+np.cross((self.v[-1]+k1v/2),self.B))*dt
        k3v=(self.q/self.m)*(self.E+np.cross((self.v[-1]+k2v/2),self.B))*dt
        k4v=(self.q/self.m)*(self.E+np.cross((self.v[-1]+k3v),self.B))*dt
        k1x=self.v[-1]*dt
        k2x=(self.v[-1]+k1v/2)*dt
        k3x=(self.v[-1]+k2v/2)*dt
        k4x=(self.v[-1]+k3v)*dt
        self.v.append(self.v[-1]+(1/6)*(k1v+2*k2v+2*k3v+k4v))
        self.x.append(self.x[-1]+(1/6)*(k1x+2*k2x+2*k3x+k4x))
        self.a.append((self.q/self.m)*(self.E+np.cross(self.v[-1],self.B)))

    def Runge_trajectory(self,dt,t):
        for i in np.arange(0,t,dt):
            self.__Rungemove(dt)
        z=[i[2] for i in self.x]
        y=[i[1] for i in self.x]
        x=[i[0] for i in self.x]
        return x,y,z



    