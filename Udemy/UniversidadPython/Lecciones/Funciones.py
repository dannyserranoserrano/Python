# Funciones
def miFuncion():
    print('Saludos desde mi funcion')


miFuncion()


# Con Parametros
def miFuncion(nombre, apellido):
    print('Saludos desde mi funcion')
    print(f'Nombre: {nombre}, Apellido: {apellido}')


miFuncion("Danny", "Serrano")
miFuncion('Clara', 'Lara')


# Return en funciones
def sumar(a=0, b=0):
    return a + b


resultado = sumar()

print(f'Resultado de la suma: {resultado}')

# Valores por default
print(f'Resultado de la suma: {sumar(2,8)}')
