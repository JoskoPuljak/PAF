check=False
pokusaj_ponovno=False
while check==False:
    if pokusaj_ponovno==True:
        print("Pokusaj ponovno")
    c=input("Upisi u formatu x,y koordinate prve tocke")
    if len(c)!=2:
        check=False
    elif isinstance(c[0],int)==False or isinstance(c[1],int)==False:
        check=False
    else:
        check=True
    pokusaj_ponovno=True
check=False
pokusaj_ponovno=False
while check==False:
    if pokusaj_ponovno==True:
        print("Pokusaj ponovno")
    d=input("Upisi u fomatu x,y koordinate druge tocke")
    if len(d)!=2:
        check=False
    elif isinstance(d[0],int)==False or isinstance(d[1],int)==False:
        check=False
    else:
        check=True
    pokusaj_ponovno=True


a=tuple(int(item) for item in c)
b=tuple(int(item) for item in d)
k=(float(b[1])-float(a[1]))/(float(b[0])-float(a[0]))
l=float(a[1])-k*float(a[0])
print ("Pravac je y={}x+{}".format(k,l))
