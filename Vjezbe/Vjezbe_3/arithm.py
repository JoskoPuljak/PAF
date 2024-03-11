#a)
import math as mt
def aritm_sred(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    lista=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
    sum=0
    for i in lista:
        sum+=i
    sredina=sum/len(lista)
    return(sredina)


def stand_dev(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    lista=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
    sum=0
    for i in lista:
        sum+=(i-aritm_sred(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10))**2
    standardna=mt.sqrt(sum/(len(lista)*(len(lista)-1)))
    return(standardna)



    
