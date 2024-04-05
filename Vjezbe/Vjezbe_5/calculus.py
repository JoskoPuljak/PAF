import numpy as np
import matplotlib.pyplot as plt
def derivacija_tocka(funkc,x,two_step="No"):
    dx=0.1
    if two_step=="No":
        deriv=(funkc(x+dx)-funkc(x-dx))/(2*dx)
    else:
        deriv=(funkc(x+dx)-funkc(x))/dx
    return deriv
def derivacija(funkc,x0,x1,epsilon,two_step="No"):
    dx=0.1
    step=round((x1-x0)/epsilon)
    x=np.linspace(x0,x1,step)
    deriva=[]
    if two_step=="No":
        for i in x:
            d=(funkc(i+dx)-funkc(i-dx))/(2*dx)
            deriva.append(d)
    else:
        for i in x:
            d=(funkc(i+dx)-funkc(i))/dx
            deriva.append(d)
    return x,np.array(deriva)
def pravokutna_integracija(funkc,x1,x2,n):
    deltax=(x2-x1)/n
    Donja=sum([funkc(i)*deltax for i in np.linspace(x1,x2-deltax,n)])
    Gornja=sum([funkc(i)*deltax for i in np.linspace(x1+deltax,x2,n)])
    return Donja,Gornja
def trapezna_integracija(funkc,x1,x2,n):
    deltax=np.linspace(x1,x2,n)[1]-np.linspace(x1,x2,n)[0]
    Int=(deltax)*(sum([funkc(i) for i in np.linspace(x1,x2,n)[1:-1]])+(funkc(x1)+funkc(x2))/2)

    return Int

