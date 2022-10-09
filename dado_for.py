import random
n=int(input("cuantas veces lanzará el dado: "))
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0

for i in range (n):
    d= random.randint(1,6)
    if d==1:
        c1=c1+1
    elif d==2:
        c2=c2+1
    elif d==3:
        c3=c3+1
    elif d==4:
        c4=c4+1
    elif d==5:
        c5=c5+1
    elif d==6:
        c6=c6+1

print(c1,c2,c3,c4,c5,c6)


