estudiante={
    'nombre':'juan',
    'edad':22,
    'es futbolista': True,
}

print(estudiante )

print(estudiante['nombre'])

print(estudiante.get('edad'))

#recorrer un diccionario y obtener sus valores 

for valor in estudiante.values():
    print(valor)
    
    