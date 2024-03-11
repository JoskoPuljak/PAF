import numpy as np
import matplotlib.pyplot as plt
def lin_regress(phi,M):
    prod_list=[i*j for i,j in zip(phi,M)]
    product_mean=np.mean(prod_list)
    x_square_list=[i**2 for i in phi]
    x_square_mean=np.mean(x_square_list)
    slope=product_mean/x_square_mean
    kx=[slope*i for i in phi]
    
    
    plt.plot(phi,kx)
    plt.show()


        