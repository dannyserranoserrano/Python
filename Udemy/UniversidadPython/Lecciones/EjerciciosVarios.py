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

#Ejercicio Calificaciones
while True:
    nota = int(input("Introduce tu nota: "))
    if 9 <= nota <= 10:
        print(f'Tu nota {nota} es una A')
    elif 8 <= nota < 9:
        print(f'Tu nota {nota} es una B')
    elif 7 <= nota < 8:
        print(f'Tu nota {nota} es una C')
    elif 6 <= nota < 7:
        print(f'Tu nota {nota} es una D')
    elif 0 <= nota < 6:
        print(f'Tu nota {nota} es una F')
    else:
        print(f'Tu nota {nota} es Valor Incorrecto')
