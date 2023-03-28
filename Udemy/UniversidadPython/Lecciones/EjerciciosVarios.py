import os

# #Ejercicio Tienda de Libros
# print('Proporciona los siguientes datos del libro')
# titulo = input('Proporciona el nombre: ')
# id = int(input('Proporciona el Id: '))
# precio = float(input('Proporciona el precio: '))
# envio = input('Indica si el envio es gratuito (True/False): ')
#
# if (envio == "True"):
#     envio = True
# elif (envio == "False"):
#     envio = False
# else:
#     envio = input("Valor incorrecto, introduce True o False: ")
#     if (envio == "True"):
#         envio = True
#     elif (envio == "False"):
#         envio = False
#     else:
#         envio = "Valor incorrecto"
# print(f'''
#     Nombre: {titulo}
#     Id: {id}
#     Precio: {precio}
#     Envio Gratuito: {envio}
# ''')


# # Calcular la estacion segun el mes proporcionado
# mes = int(input('Proporciona mes del año (1-12): '))
# estacion = None #None es equivalente a null en javascript
# if mes == 1 or mes == 2 or mes == 12:
#     estacion = "Invierno"
# elif  mes == 3 or mes == 4 or mes == 5:
#     estacion = "Primavera"
# elif  mes == 6 or mes == 7 or mes == 8:
#     estacion = "Verano"
# elif  mes == 9 or mes == 10 or mes == 11:
#     estacion = "Otoño"
# else:
#     estacion = "Mes Incorrecto"
# print(f'Para el mes {mes} la estacion es: {estacion}')

# #Ejercicio Proporciona tu edad
# while True:
#     edad = int(input("Proporciona tu edad: "))
#     if 0 <= edad < 10:
#         print("La infancia es increible")
#     elif 10 <= edad < 20:
#         print("Muchos cambios y mucho estudio")
#     elif 20 <= edad < 30:
#         print("Amor y comienza el trabajo")
#     else:
#         print("Etapa de vida no reconocida")

# #Ejercicio Calificaciones
# while True:
#     nota = int(input("Introduce tu nota: "))
#     if 9 <= nota <= 10:
#         print(f'Tu nota {nota} es una A')
#     elif 8 <= nota < 9:
#         print(f'Tu nota {nota} es una B')
#     elif 7 <= nota < 8:
#         print(f'Tu nota {nota} es una C')
#     elif 6 <= nota < 7:
#         print(f'Tu nota {nota} es una D')
#     elif 0 <= nota < 6:
#         print(f'Tu nota {nota} es una F')
#     else:
#         print(f'Tu nota {nota} es Valor Incorrecto')
#
# #Ejercicios Listas.
#     #Ejercicio 1.
#         #Iterar un rango de numeros de 0 a 10 e imprimir números divisibles entre 3
# for numero in range(11):
#     if numero % 3 == 0:
#         print(numero)
#
#     #Ejercicio 2.
#         #Crear un rango de números de 2 a 6, e imprimirlos.
# for numero in range(2, 7):
#     print(numero)
#
#     #Ejercicio 3.
#         #Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1.
# for numero in range(3, 11, 2):
#     print(numero)

# #Ejercicio Tuplas
# #Dada la siguiente tupla, crear una lista que solo incluya los numeros menores a 5
# tupla = (13, 1, 8, 3, 2, 5, 8)
# lista = []
# print(f'Tupla creada: {tupla}')
# for number in tupla:
#     if number < 5:
#         lista.append(number)
# print(f'Lista resultante: {lista}')

# #Ejercicos Funciones
#     #Crear una funcion para sumar los valores recibidos de tipo numérico,
#     #utilizando argumentos variables *args como parámetro de la función
#     #y regresar como resultado la suma de todos los valores pasados como argumentos.
#
# def sumas(*numeros):
#     resultado = 0
#     for numero in numeros:
#         resultado += numero
#     #print(resultado)
#     return resultado
# #sumas(5, 6, 8, 25, 45)
# print(sumas(5, 6, 8, 25, 450))

# #Ejercicio multiplicar
#     #Crear funcion multiplicar los valores recibidos, utilizando *args como parametros
#
# def multiplica(*args):
#     resultado = 1
#     for numero in args:
#         resultado *= numero
#     return resultado
# print(multiplica(5, 6, 43, 3, 45))
#

# #Ejercicio Funcion recursiva
#     #  Imprimir numeros de 5 a 1 de manera descendiente usando funciones recursivas.
# def imprDescendiente(numero):
#     if numero >= 1:
#         print(numero)
#         imprDescendiente(numero - 1)
#     elif numero == 0:
#         return
#     elif numero < 0:
#         print('Valor incorrecto...')
# numero = 0
# imprDescendiente(numero)

# #Ejercicio Calculadora de Impuestos
#     #Funcion calcular total de un pago incluyendo un impuesto aplicado.
#     #Formula: pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
# def calculadoraImpuestos(pago, impuestos):
#     pagoTotal = pago + pago * (impuestos/100.0)
#     return pagoTotal
#
# pago = float(input("Proporciona el pago sin impuesto: "))
# impuestos = float(input("Proporciona el valor del impuesto: "))
# pagoTotal = calculadoraImpuestos(pago, impuestos)
# print(f'Pago con Impuestos: {pagoTotal}')

