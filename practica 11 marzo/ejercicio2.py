listanumeros =[]
for i in range(0,5,1):
    numeroingresado= int(input("ingrese el numero: "))
    listanumeros.append(numeroingresado)

buscarnumero= int(input("¿Que numero desea buscar"))

for i in range(0,5,1):
    if(buscarnumero in listanumeros):

        print("Si esta en la lista")
else:
    print("No esta en la lista")
