#funkcija
def mjerac_greske(N):
    a=5
    for i in range (N):
        a+=1/3
    for j in range(N):
        a+=-1/3
    return(a)
print(mjerac_greske(200))
print(mjerac_greske(2000))
print(mjerac_greske(20000))
#pri manjem broju ponavljanja, nepreciznost floata se uočava tek pri 16-oj znamenci,a kod 20000 ponavljanja, nepreciznost je ma 14-oj
if mjerac_greske(200)==5:
    print("da")
if mjerac_greske(2000)==5:
    print("da")
if mjerac_greske(20000)==5:
    print("da")
#nije dovoljno blizu da ga prepoznaje kao isti broj ni u jednom slučaju