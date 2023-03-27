nombres = ['Juan', 'Carla', 'Ricardo', 'Maria']

# Imprimir la lista de nombres
print(nombres)

# Acceder a los elementos de la lista
print(nombres[0])
print(nombres[1])
print(nombres[2])

# Acceder a los elementos de forma inversa
print(nombres[-1])
print(nombres[-2])

# Imprimir un rango
print(nombres[0:2])  # Sin incluir el indice 2

# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[: 3])

# Desde el indice indicado hasta el final
print(nombres[1:])

# Cambiar valor
nombres[3] = 'Ivone'
print(nombres)

# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')

# Preguntar el largo de una lista
print(len(nombres))

# Agregar un elemento
nombres.append(('Lorenzo'))
print(nombres)

# Insertar un elemento en un indice en especifico
nombres.insert(1, 'Octavio')
print(nombres)

# Remover un elemento
nombres.remove('Octavio')
print(nombres)

# Remover el ultimo valor agregado
nombres.pop()
print(nombres)

# Eliminar elemento en un indice determinado
del nombres[0]
print(nombres)

# limpiar la lista
nombres.clear()
print(nombres)

# Borrar la lista por completo
del nombres
print(nombres)
