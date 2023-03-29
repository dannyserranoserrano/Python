#Set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

#Largo
print(len(planetas))

#Revisar si un elemento esta presente
print("Marte" in planetas)

#Agregar un elemento
planetas.add('Tierra')
print(planetas)

#No se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)

#Eliminar elementos posiblemente arrojando error
planetas.remove('Tierra')
print(planetas)
#Eliminar elementos sin arrojarx error
planetas.discard('Jupiter')
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#eliminar el set
del planetas
print(planetas)
