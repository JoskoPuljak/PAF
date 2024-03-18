class Particle:
    def __init__(self,mass,x_0,v):
        self.mass=mass
        self.x_0=x_0
        self.v=v
    def printinfo(self):
        print("Masa cestice=",self.mass)
        print("Polozaj cestice=",self.x_0)
        print("Brzina cestice=",self.v)
    def ishodiste(self):
        self.x_0=0
    def ubrzaj(self,deltav):
        self.v+=deltav
    
cest1=Particle(10,10,20)
cest1.printinfo()
cest1.ishodiste()
cest1.ubrzaj(5)
cest1.printinfo()