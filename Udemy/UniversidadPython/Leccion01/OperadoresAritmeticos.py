operandoA = 3
operandoB = 2
suma = operandoA + operandoB
#print('Resultado Suma:', suma)
print(f'Resultado suma: {suma}')
resta = operandoA - operandoB
print(f'Resultado resta: {resta}')
multiplicacion = operandoA * operandoB
print(f'Resultado multiplicacion: {multiplicacion}')
division  = operandoA / operandoB
print(f'Resultado division: {division}')
division = operandoA // operandoB
print(f'Resultado division (int): {division}')
modulo = operandoA % operandoB
print(f'Resultado modulo o Resto de la division: {modulo}')
exponente = operandoA ** operandoB
print(f'Resultado exponente: {exponente}')

# Ejercicio Calcula el area y el perimetro de un triangulo

alto = int(input("Proporciona el alto del rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))
Area = alto * ancho
Perimetro = (2*ancho)+(2*alto)
print(f'El Area es: {Area}')
print(f'El Perimetro es: {Perimetro}')
