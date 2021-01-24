dalcom = int(input())

fivebag = dalcom//5
dalcom %= 5
threebag = 0

while fivebag >= 0:
    if dalcom%3 == 0:
        threebag = dalcom//3
        dalcom = 0
        break
    fivebag-=1
    dalcom+=5
print((dalcom==0)and(fivebag+threebag) or -1)
