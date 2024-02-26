#######Neurednije, ali točnije rješenje#########################

check=False
while check==False:
    x1=input("Upiši prvu koordinatu prve točke ")
    if x1.isdigit()==False:
        print("Ponovno upišite točku")
        check=False
    else:
        check=True

check=False
while check==False:
    y1=input("Upiši drugu koordinatu prve točke")
    if y1.isdigit()==False:
        print("Ponovno upišite točku")
        check=False
    else:
        check=True

check=False
while check==False:
    x2=input("Upiši prvu koordinatu druge točke ")
    if x2.isdigit()==False:
        print("Ponovno upišite točku")
        check=False
    else:
        check=True
check=False
while check==False:
    y2=input("Upiši drugu koordinatu druge točke")
    if y2.isdigit()==False:
        print("Ponovno upišite točku")
        check=False
    else:
        check=True

k=(int(y2)-int(y1))/(int(x2)-int(x1))
l=int(y1)-k*int(x1)
print ("Pravac je y={}x+{}".format(k,l))
