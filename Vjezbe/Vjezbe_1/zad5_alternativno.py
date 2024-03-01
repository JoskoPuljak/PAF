#Saveanje i  showanje se pita od korisnika kao input svaki put kad se passa funkcija

import matplotlib.pyplot as plt
def pravac(a,b):
    k=(float(b[1])-float(a[1]))/(float(b[0])-float(a[0]))
    l=float(a[1])-k*float(a[0])
    print ("Pravac je y={}x+{}".format(k,l))
    plt.plot([a[0],b[0]],[a[1],b[1]])
    a=input("Želiš li spremiti u pdf?")
    if a.lower()=="da":
        b=input("Imenujte file")
        plt.savefig("{}.pdf".format(b), format="pdf")
    else:
        plt.show()

pravac((1,2),(3,3))
