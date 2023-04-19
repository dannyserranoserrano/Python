# from Cuadrado import Cuadrado
from EjercicioHerenciaMultiple import *

print('Creacion Objeto Cuadrado'.center(50, '-'))
# print(f'Calculo del area cuadrado: {cuadrado1.calcularArea()}')
cuadrado1 = Cuadrado(5, 'rojo')
print(f'Calculo del area cuadrado: {cuadrado1.area()}')
print(cuadrado1)

rectangulo1 = Rectangulo(5, 6, 'azul')
print('Creacion Objeto Rectangulo'.center(50, '-'))
print(f'Calculo del area rectangulo: {rectangulo1.area()}')
print(rectangulo1)

# #MRO - Method Resolution Order
# print(Cuadrado.mro())