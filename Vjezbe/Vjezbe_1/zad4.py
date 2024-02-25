def pravac(a,b):
    k=(float(b[1])-float(a[1]))/(float(b[0])-float(a[0]))
    l=float(a[1])-k*float(a[0])
    print ("Pravac je y={}x+{}".format(k,l))

pravac((1,2),(3,3))

