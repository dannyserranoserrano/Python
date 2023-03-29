#Definir una tupla
frutas = ('Naranja', 'Platano', 'Melon')
print(frutas)

#Saber el largo
print(len(frutas))

#acceder a un elemento
print(frutas[0])

#Navegacion inversa
print(frutas[-2])

#Acceder a un rango
print(frutas[0:1])#Sin incluir el ultimo numero

#Recorrer elementos
for fruta in frutas:
    print(fruta, end=' ')

#Cambiar valor tupla
# frutas[0] = 'Pera'
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n', frutas)

#Eliminar tupla por completo
del frutas
print(frutas)
