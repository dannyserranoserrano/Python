a = 4
b = 2

resultado = (a == b)
print(f'Resultado == : {resultado}')

resultado = (a != b)
print(f'Resultado != : {resultado}')

resultado = (a > b)
print(f'Resultado > : {resultado}')

resultado = (a <= b)
print(f'Resultado <= : {resultado}')

#Ejercicio Algoritmo Par_impar
a = int(input("Escribe un valor numerico: "))

if (a % 2 == 0):
    print(f'El numero {a} es Par')
else:
    print(f'El numero {a} es Impar')

#Ejercicio Algoritmo Determinar Mayor de Edad
edadAdulto = 18
edadPersona = int(input("Proporciona tu edad: "))
print('Eres mayor de edad') if edadPersona >= edadAdulto else print('Eres menor de edad')