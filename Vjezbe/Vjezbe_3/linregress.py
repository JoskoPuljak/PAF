import numpy as np
import matplotlib.pyplot as plt
def lin_regress(x,y,colour="red",xlabel="x os", ylabel="y os", title="x/y graf",linelegend="graf linearne regresije",scatterlegend="pravi podaci"):
    prod_list=[i*j for i,j in zip(x,y)]
    product_mean=np.mean(prod_list)
    x_square_list=[i**2 for i in x]
    x_square_mean=np.mean(x_square_list)
    slope=product_mean/x_square_mean
    kx=[slope*i for i in x]
    
    
    plt.plot(x,kx,color=colour)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.scatter(x,y)
    plt.legend([linelegend,scatterlegend])
    plt.show()


        