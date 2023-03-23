a = False
b = True
resultado  = a and b
print(resultado)

resultado  = a or b
print(resultado)

resultado  = not a
print(resultado)
resultado  = not b
print(resultado)

#Ejercicio Valor dentro del rango
valor = int(input('Introduce un digito: '))
valorMin = 0
valorMax = 5

dentroRango = (valor >= valorMin) and (valor <= valorMax)
print(f'El valor {valor} está dentro de rango ') if dentroRango else print(f'El valor {valor} está fuera de rango ')

#Ejercicio con operador OR
vacaciones = True
diaDescanso = True

print('No puede asistir al partido') if not (vacaciones or diaDescanso) else print('Puede asistir al partido')

#Ejercicio AND OR
edad = int(input("Introduce tu edad: "))
veintes = edad >= 20 and edad < 30
treintas = edad >= 30  and edad < 40
print('Dentro de los rangos (20\'s o 30\'s)') if veintes or treintas else print("No está dentro de los 20's ni 30's")

#Otras formas
if(20 <= edad < 30) or (30 <= edad <40):
    print('Dentro de rango (20\'s) o (30\'s)')
else:
    print("No está dentro de los 20's ni 30's")

#Ejercicio Cual es mayor
valor1 = int(input("Introduce el primer valor: "))
valor2 = int(input("Introduce el segundo valor: "))

if(valor1 > valor2):
    print(f'{valor1} es superior a {valor2}: ')
elif(valor1 < valor2):
    print(f'{valor2} es superior a {valor1}: 4')
else:
    print(f'{valor1} es igual a {valor2}')


