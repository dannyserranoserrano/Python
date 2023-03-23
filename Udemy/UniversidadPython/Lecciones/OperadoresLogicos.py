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
diaDescanso = False

print('Puede asistir al partido') if vacaciones or diaDescanso else print('No puede asistir al partido')
