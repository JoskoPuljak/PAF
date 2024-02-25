import matplotlib.pyplot as plt
def pravac(a,b,c="show"):
    k=(float(b[1])-float(a[1]))/(float(b[0])-float(a[0]))
    l=float(a[1])-k*float(a[0])
    print ("Pravac je y={}x+{}".format(k,l))
    plt.plot([a[0],b[0]],[a[1],b[1]])
    if c=="show":
        plt.show()
    else:
        plt.savefig("{}.pdf.".format(c), format="pdf")

pravac((1,2),(3,3),"pravac")
