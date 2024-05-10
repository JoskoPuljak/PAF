import numpy as np
import matplotlib.pylot as plt
import matplotlib.animation as ani

class duplo_njihalo:
    def __init__(self,l1,l2,theta1,theta2,phi1,phi2):
        self.l1=l1
        self.l2=l2
        self.theta1=[theta1]
        self.theta2=[theta2]
        self.phi1=[phi1]
        self.phi2=[phi2]
        self.g=9.81
        self.alpha1=[]
        self.alpha2=[]
        self.x=[]
        self.v=[]
        self.a=[]
    def reset(self):
        self.theta1=[theta1]
        self.theta2=[theta2]
        self.phi1=[phi1]
        self.phi2=[phi2]
        self.alpha1=[]
        self.alpha2=[]
        self.x=[]
        self.v=[]
        self.a=[]
    def __move(self,dt):
    
    def plot_trajectory(self,dt,t):

