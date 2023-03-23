#Ejercicio Tienda de Libros
print('Proporciona los siguientes datos del libro')
titulo = input('Proporciona el nombre: ')
id = int(input('Proporciona el Id: '))
precio = float(input('Proporciona el precio: '))
envio = input('Indica si el envio es gratuito (True/False): ')

if (envio == "True"):
    envio = True
elif (envio == "False"):
    envio = False
else:
    envio = input("Valor incorrecto, introduce True o False: ")
    if (envio == "True"):
        envio = True
    elif (envio == "False"):
        envio = False
    else:
        envio = "Valor incorrecto"
print(f'''
    Nombre: {titulo}
    Id: {id}
    Precio: {precio}
    Envio Gratuito: {envio}
''')
