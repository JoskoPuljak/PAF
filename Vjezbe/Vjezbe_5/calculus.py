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



