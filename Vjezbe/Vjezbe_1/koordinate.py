
a=input("Upisi u formatu (x,y) koordinate prve tocke")
if isinstance(a,tuple)==False:
    print("yoo")
    print("Ponvno upisite, pogresno ste upisali")
    a=input("Upisi u formatu (x,y) koordinate prve tocke")
elif isinstance(a[0],float)==False or isinstance(a[1],float)==False:
    print("Ponvno upisite, pogresno ste upisali")
    a=input("Upisi u formatu (x,y) koordinate prve tocke")
b=input("Upisi u fomatu (x,y) koordinate druge tocke")
if isinstance(b,tuple)==False:
    print("Ponvno upisite, pogresno ste upisali")
    b=input("Upisi u formatu (x,y) koordinate druge tocke")
elif isinstance(b[0],float)==False or isinstance(b[1],float)==False:
    print("Ponvno upisite, pogresno ste upisali")
    b=input("Upisi u formatu (x,y) koordinate druge tocke")
k=(float(b[1])-float(a[1]))/(float(b[0])-float(a[0]))
l=float(a[1])-k*float(a[0])
print ("Pravac je y={}x+{}".format(k,l))

