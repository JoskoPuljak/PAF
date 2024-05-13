import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

class duplo_njihalo:
    def __init__(self,m1,m2,l1,l2,theta1,theta2,phi1,phi2):
        self.m1=m1
        self.m2=m2
        self.l1=l1
        self.l2=l2
        self.theta1=[np.radians(theta1)]
        self.theta2=[np.radians(theta2)]
        self.phi1=[phi1]
        self.phi2=[phi2]
        self.g=9.81
        self.alpha1=[(-self.g*(2*self.m1+self.m2)*np.sin(self.theta1[0])-m2*self.g*np.sin(self.theta1[0]-2*self.theta2[0])-2*np.sin(self.theta1[0]-2*self.theta2[0]*self.m2*(self.theta2[0]**2)*self.l2+(self.theta1[0]**2)*self.l1*np.cos(self.theta1[0]-self.theta2[0])))/(self.l1*(2*self.m1+self.m2-self.m2*np.cos(2*self.theta1[0]-2*self.theta2[0])))]
        self.alpha2=[(2*np.sin(self.theta1[0]-self.theta2[0])*((self.theta1[0]**2)*self.l1*(self.m1+self.m2)+self.g*(self.m1+self.m2)*np.cos(self.theta1[0])+(self.theta2[0]**2)*self.l2*self.m2*np.cos(self.theta1[0]-self.theta2[0])))/(self.l2*(2*self.m1+self.m2-self.m2*np.cos(2*self.theta1[0]-2*self.theta2[0])))]
        self.x1=[]
        self.x2=[]
    def reset(self):
        self.theta1=[theta1[0]]
        self.theta2=[theta2[0]]
        self.phi1=[phi1[0]]
        self.phi2=[phi2[0]]
        self.alpha1=[alpha1[0]]
        self.alpha2=[alpha1[0]]
        self.x1=[]
        self.x2=[]
    def move(self,dt):
        self.x1.append(np.array([self.l1*np.sin(self.theta1[-1]),-self.l1*np.cos(self.theta1[-1])]))
        self.x2.append(self.x1[-1]+np.array([self.l2*np.sin(self.theta2[-1]),-self.l2*np.cos(self.theta2[-1])]))
        self.phi1.append(self.phi1[-1]+self.alpha1[-1]*dt)
        self.phi2.append(self.phi2[-1]+self.alpha2[-1]*dt)
        self.theta1.append(self.theta1[-1]+self.phi1[-1]*dt)
        self.theta2.append(self.theta2[-1]+self.phi2[-1]*dt)
        self.alpha1.append((-self.g*(2*self.m1+self.m2)*np.sin(self.theta1[-1])-self.m2*self.g*np.sin(self.theta1[-1]-2*self.theta2[-1])-2*np.sin(self.theta1[-1]-2*self.theta2[-1]*self.m2*(self.theta2[-1]**2)*self.l2+(self.theta1[-1]**2)*self.l1*np.cos(self.theta1[-1]-self.theta2[-1])))/(self.l1*(2*self.m1+self.m2-self.m2*np.cos(2*self.theta1[-1]-2*self.theta2[-1]))))
        self.alpha2.append((2*np.sin(self.theta1[-1]-self.theta2[-1])*((self.theta1[0]**2)*self.l1*(self.m1+self.m2)+self.g*(self.m1+self.m2)*np.cos(self.theta1[-1])+(self.theta2[-1]**2)*self.l2*self.m2*np.cos(self.theta1[-1]-self.theta2[-1])))/(self.l2*(2*self.m1+self.m2-self.m2*np.cos(2*self.theta1[-1]-2*self.theta2[-1]))))
    def plot_trajectory(self,dt,t):
        for i in np.arange(0,t,dt):
            self.move(dt)
        #print(self.x1)
        x1=np.array(self.x1)[:,0]
        y1=np.array(self.x1)[:,1]
        x2=np.array(self.x2)[:,0]
        y2=np.array(self.x2)[:,1]
        
        plt.rcParams["figure.figsize"] = [5, 5]
        plt.rcParams["figure.autolayout"] = True
        fig=plt.figure()
        ax=plt.axes(xlim=(-0.1,0.1),ylim=(-0.1,0.1))

        line,=ax.plot([],[],"o",color="blue")
        line2,=ax.plot([],[],"o",color="blue")
        
        def init():
            line.set_data([],[])
            line2.set_data([],[])
            return line,line2

        def animate(i):
            x_1=x1[i]
            y_1=y1[i]
            line.set_data(x_1,y_1)
            x_2=x2[i]
            y_2=y2[i]
            line2.set_data(x_2,y_2)
            return line,line2
        anim = ani.FuncAnimation(fig, animate, init_func=init, frames=100000, interval=50, blit=True)
        
        plt.show()


Njihy=duplo_njihalo(0.1,0.1,0.05,0.05,40,20,0.5,0.1)
Njihy.plot_trajectory(0.01,15)

