#test 5.0-4.935
print(5.0-4.395)
#ocekujem 0.605 a dobijam 0.605 s puno nula i četvorkom radi nepreciznosti floating point načina zapisa brojeva racunala na 1/2^n

#test je li 0.1+0.2+0.3 isto sto i 0.6
s=0.1+0.2+0.3
if s==0.6:
    print("Zbroj je 0.6")
else:
    print("Zbroj nije 0.6")
#dobili smo da broj nije 0.6 zbog floating point nepreciznosti

