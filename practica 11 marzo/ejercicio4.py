listanumeros =[]
for i in range(0,5,1):
    numeroingresado= int(input("ingrese el numero: "))
    listanumeros.append(numeroingresado)

buscarnumero= int(input("Que numero desea buscar: "))

flag=False

for numero in listanumeros:
    if(buscarnumero == numero):
        flag=True
        break
    else:
        flag=False
if(flag != False):
    print("si esta el numero")
else:
    print("no esta")
