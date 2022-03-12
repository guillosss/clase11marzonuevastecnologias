estudiantes=('carlos','pedro')

for estudiante in estudiantes:
    print(estudiante)

#convirtiendo una tupla en un arreglo 

listaEstudiantes=list(estudiantes)
print(listaEstudiantes)

listaEstudiantes.append(input("Ingrese estudiante"))

newTuple=tuple(listaEstudiantes)

print(newTuple)
