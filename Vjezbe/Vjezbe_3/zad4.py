import linregress as lin
M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]
lin.lin_regress(M,phi,"purple", "$\\varphi$ /rad", "M/Nm","M/phi graf","pravac linearne regresije M/$\\varphi$", "prave vrijednosti M")