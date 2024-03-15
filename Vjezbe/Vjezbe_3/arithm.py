#a)
import math as mt
def aritm_sred(lista):
    sum=0
    for i in lista:
        sum+=i
    sredina=sum/len(lista)
    return(sredina)


def stand_dev(lista):
    sum=0
    for i in lista:
        sum+=(i-aritm_sred(lista))**2
    standardna=mt.sqrt(sum/(len(lista)*(len(lista)-1)))
    return(standardna)



    
