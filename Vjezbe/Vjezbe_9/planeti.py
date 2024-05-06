import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class dvaplaneta:
    def __init__ (self,x_Sunce,x_Zemlja,v0_Zemlja):
        self.G=6.67408*(10**(-11))
        self.Ms=1.989*(10**30)
        self.Mz=5.9742*(10**24)
        self.x_Sunce=[np.array(x_Sunce)]
        self.x_Zemlja=[np.array(x_Zemlja)]
        self.v_Zemlja=[np.array((0,v0_Zemlja))]
        self.v_Sunce=[np.array((0,0))]
        self.a_Sunce=[(-self.G*(self.Mz)/(np.linalg.norm(self.x_Zemlja[0]-self.x_Sunce[0]))**3)*(self.x_Sunce[0]-self.x_Zemlja[0])]
        self.a_Zemlja=[(-self.G*(self.Ms)/(np.linalg.norm(self.x_Zemlja[0]-self.x_Sunce[0]))**3)*(self.x_Zemlja[0]-self.x_Sunce[0])]
    def reset(self):
        self.x_Sunce=[self.x_Sunce[0]]
        self.x_Zemlja=[self.x_Zemlja[0]]
        self.v0_Zemlja=[self.v_Zemlja[0]]
        self.v_Sunce=[self.v_Sunce[0]]
        self.a_Sunce=[self.a_Sunce[0]]
        self.a_Zemlja=[self.a_Zemlja[0]]
    def __move(self,dt):
        self.v_Sunce.append(self.v_Sunce[-1]+self.a_Sunce[-1]*dt)
        self.v_Zemlja.append(self.v_Zemlja[-1]+self.a_Zemlja[-1]*dt)
        self.x_Sunce.append(self.x_Sunce[-1]+self.v_Sunce[-1]*dt)
        self.x_Zemlja.append(self.x_Zemlja[-1]+self.v_Zemlja[-1]*dt)
        self.a_Sunce.append((-self.G*(self.Mz)/(np.linalg.norm(self.x_Zemlja[-1]-self.x_Sunce[-1]))**3)*(self.x_Sunce[-1]-self.x_Zemlja[-1]))
        self.a_Zemlja.append((-self.G*(self.Ms)/(np.linalg.norm(self.x_Zemlja[-1]-self.x_Sunce[-1]))**3)*(self.x_Zemlja[-1]-self.x_Sunce[-1]))
        
    def plot_trajectory(self,dt,t):
        for i in np.arange(0,t,dt):
            self.__move(dt)
        xs=np.array(self.x_Sunce)[:,0]
        ys=np.array(self.x_Sunce)[:,1]
        xz=np.array(self.x_Zemlja)[:,0]
        yz=np.array(self.x_Zemlja)[:,1]
        
        plt.rcParams["figure.figsize"] = [5, 5]
        plt.rcParams["figure.autolayout"] = True
        fig=plt.figure()
        ax=plt.axes(xlim=(-1.486*(10**11),1.486*(10**11)),ylim=(-1.486*(10**11),1.486*(10**11)))
        plotted=ax.plot(xz,yz)

        line,=ax.plot([],[],"o",color="blue")
        line2,=ax.plot([],[],"o",color="yellow")
        
        def init():
            line.set_data([],[])
            line2.set_data([],[])
            return line,line2

        def animate(i):
            x=xz[i]
            y=yz[i]
            line.set_data(x,y)
            x2=xs[i]
            y2=ys[i]
            line2.set_data(x2,y2)
            return line,line2
        anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100000, interval=1, blit=True)
        ax.set_xlabel("x/m")
        ax.set_ylabel("y/m")
        ax.set_title("Gibanje Zemlje oko Sunca")
        plt.legend(["putanja Zemlje","Zemlja","Sunce"])
        plt.show()
        
  
        

