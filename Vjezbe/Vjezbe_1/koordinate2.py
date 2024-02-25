def format_check(input):
    check=True
    for i in input:
        if input.isnumeric()==False and input!= ",":
            check=False
    return check

c=(input("Upisi u formatu x,y koordinate prve tocke"))
while format_check(c)==False:
    print("Pokušajte ponovno")
    c=(input("Upisi u formatu x,y koordinate prve tocke"))

d=(input("Upisi u fomatu x,y koordinate druge tocke"))
while format_check(d)==False:
    print("Pokušajte ponovno")
    d=(input("Upisi u formatu x,y koordinate prve tocke"))

check=True

a=tuple(int(item) for item in c.split(","))
b=tuple(int(item) for item in d.split(","))
k=(float(b[1])-float(a[1]))/(float(b[0])-float(a[0]))
l=float(a[1])-k*float(a[0])
print ("Pravac je y={}x+{}".format(k,l))




