import random
n=int(input("cuantas veces lanzará el dado: "))
c1=""
c2=""
c3=""
c4=""
c5=""
c6=""

for i in range (n):
    d= random.randint(1,6)
    if d==1:
        c1=c1+"*"
    elif d==2:
        c2=c2+"*"
    elif d==3:
        c3=c3+"*"
    elif d==4:
        c4=c4+"*"
    elif d==5:
        c5=c5+"*"
    elif d==6:
        c6=c6+"*"

print("Cara Numero 1: ",c1)
print("Cara Numero 2: ",c2)
print("Cara Numero 3: ",c3)
print("Cara Numero 4: ",c4)
print("Cara Numero 5: ",c5)
print("Cara Numero 6: ",c6)



