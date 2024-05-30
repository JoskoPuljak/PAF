import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

class duplo_njihalo:
    def __init__(self,m1,m2,l1,l2,theta1,theta2,omega1,omega2):
        self.m1=m1
        self.m2=m2
        self.l1=l1
        self.l2=l2
        self.theta1=[np.radians(theta1)]
        self.theta2=[np.radians(theta2)]
        self.omega1=[omega1]
        self.omega2=[omega2]
        self.g=9.81
        self.alpha1=[(-self.g*(2*self.m1+self.m2)*np.sin(self.theta1[0])-m2*self.g*np.sin(self.theta1[0]-2*self.theta2[0])-2*np.sin(self.theta1[0]-2*self.theta2[0]*self.m2*(self.theta2[0]**2)*self.l2+(self.theta1[0]**2)*self.l1*np.cos(self.theta1[0]-self.theta2[0])))/(self.l1*(2*self.m1+self.m2-self.m2*np.cos(2*self.theta1[0]-2*self.theta2[0])))]
        self.alpha2=[(2*np.sin(self.theta1[0]-self.theta2[0])*((self.theta1[0]**2)*self.l1*(self.m1+self.m2)+self.g*(self.m1+self.m2)*np.cos(self.theta1[0])+(self.theta2[0]**2)*self.l2*self.m2*np.cos(self.theta1[0]-self.theta2[0])))/(self.l2*(2*self.m1+self.m2-self.m2*np.cos(2*self.theta1[0]-2*self.theta2[0])))]
        self.x1=[]
        self.x2=[]
    def reset(self):
        self.theta1=[theta1[0]]
        self.theta2=[theta2[0]]
        self.omega1=[omega1[0]]
        self.omega2=[omega2[0]]
        self.alpha1=[alpha1[0]]
        self.alpha2=[alpha1[0]]
        self.x1=[]
        self.x2=[]
    def move(self,dt):
        self.x1.append(np.array([self.l1*np.sin(self.theta1[-1]),-self.l1*np.cos(self.theta1[-1])]))
        self.x2.append(self.x1[-1]+np.array([self.l2*np.sin(self.theta2[-1]),-self.l2*np.cos(self.theta2[-1])]))
        self.omega1.append(self.omega1[-1]+self.alpha1[-1]*dt)
        self.omega2.append(self.omega2[-1]+self.alpha2[-1]*dt)
        self.theta1.append(self.theta1[-1]+self.omega1[-1]*dt)
        self.theta2.append(self.theta2[-1]+self.omega2[-1]*dt)
        self.alpha1.append((-self.g*(2*self.m1+self.m2)*np.sin(self.theta1[-1])-self.m2*self.g*np.sin(self.theta1[-1]-2*self.theta2[-1])-2*np.sin(self.theta1[-1]-2*self.theta2[-1]*self.m2*(self.theta2[-1]**2)*self.l2+(self.theta1[-1]**2)*self.l1*np.cos(self.theta1[-1]-self.theta2[-1])))/(self.l1*(2*self.m1+self.m2-self.m2*np.cos(2*self.theta1[-1]-2*self.theta2[-1]))))
        self.alpha2.append((2*np.sin(self.theta1[-1]-self.theta2[-1])*((self.theta1[0]**2)*self.l1*(self.m1+self.m2)+self.g*(self.m1+self.m2)*np.cos(self.theta1[-1])+(self.theta2[-1]**2)*self.l2*self.m2*np.cos(self.theta1[-1]-self.theta2[-1])))/(self.l2*(2*self.m1+self.m2-self.m2*np.cos(2*self.theta1[-1]-2*self.theta2[-1]))))
    def plot_trajectory(self,dt,t):
        for i in np.arange(0,t,dt):
            self.move(dt)
        x1=np.array(self.x1)[:,0]
        y1=np.array(self.x1)[:,1]
        x2=np.array(self.x2)[:,0]
        y2=np.array(self.x2)[:,1]
        
        plt.rcParams["figure.figsize"] = [5, 5]
        plt.rcParams["figure.autolayout"] = True
        fig=plt.figure()
        ax=plt.axes(xlim=(-0.1,0.1),ylim=(-0.12,0.1))
        fulcrum=ax.scatter([0],[0],color="black")
        
        line,=ax.plot([],[],"o",color="blue")
        line2,=ax.plot([],[],"o",color="blue")
        line3,=ax.plot([],[],color="black")
        line4,=ax.plot([],[],color="black")
        
        def init():
            line.set_data([],[])
            line2.set_data([],[])
            line3.set_data([],[])
            line4.set_data([],[])
            return line,line2,line3,line4

        def animate(i):
            x_1=x1[i]
            y_1=y1[i]
            line.set_data(x_1,y_1)
            x_2=x2[i]
            y_2=y2[i]
            line2.set_data(x_2,y_2)
            x_3=np.array([0,x1[i]])
            y_3=np.array([0,y1[i]])
            line3.set_data(x_3,y_3)
            x_4=np.array([x1[i],x2[i]])
            y_4=np.array([y1[i],y2[i]])
            line4.set_data(x_4,y_4)
            return line3,line4,line,line2
        anim = ani.FuncAnimation(fig, animate, init_func=init, frames=100000, interval=100, blit=True)
        plt.show()
    def plot_trace(self,dt,t):
        for i in np.arange(0,t,dt):
            self.move(dt)
        x1=np.array(self.x1)[:,0]
        y1=np.array(self.x1)[:,1]
        x2=np.array(self.x2)[:,0]
        y2=np.array(self.x2)[:,1]
        
        plt.rcParams["figure.figsize"] = [5, 5]
        plt.rcParams["figure.autolayout"] = True
        fig=plt.figure()
        ax=plt.axes(xlim=(-0.1,0.1),ylim=(-0.12,0.1))
        fulcrum=ax.scatter([0],[0],color="black")
        
        line,=ax.plot([],[],"o",color="blue")
        line2,=ax.plot([],[],"o",color="blue")
        line3,=ax.plot([],[],color="black")
        line4,=ax.plot([],[],color="black")
        line5,=ax.plot([],[],color="green")
        
        def init():
            line.set_data([],[])
            line2.set_data([],[])
            line3.set_data([],[])
            line4.set_data([],[])
            line5.set_data([],[])
            return line,line2,line3,line4,line5

        def animate(i):
            x_1=x1[i]
            y_1=y1[i]
            line.set_data(x_1,y_1)
            x_2=x2[i]
            y_2=y2[i]
            line2.set_data(x_2,y_2)
            x_3=np.array([0,x1[i]])
            y_3=np.array([0,y1[i]])
            line3.set_data(x_3,y_3)
            x_4=np.array([x1[i],x2[i]])
            y_4=np.array([y1[i],y2[i]])
            line4.set_data(x_4,y_4)
            x_5=x2[:i]
            y_5=y2[:i]
            line5.set_data(x_5,y_5)
            return line5,line3,line4,line,line2
        anim = ani.FuncAnimation(fig, animate, init_func=init, frames=100000, interval=5, blit=True)
        
        plt.show()
    def plot_picture(self,dt,t):
        for i in np.arange(0,t,dt):
            self.move(dt)
        x1=np.array(self.x1)[:,0]
        y1=np.array(self.x1)[:,1]
        x2=np.array(self.x2)[:,0]
        y2=np.array(self.x2)[:,1]
        plt.plot(x2,y2)
        plt.show()





