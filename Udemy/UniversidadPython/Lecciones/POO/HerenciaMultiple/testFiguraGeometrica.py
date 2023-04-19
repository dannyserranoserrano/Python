# from Cuadrado import Cuadrado
from EjercicioHerenciaMultiple import *

cuadrado1 = Cuadrado(5, 'rojo')
rectangulo1 = Rectangulo(5, 6, 'azul')
# print(f'Calculo del area cuadrado: {cuadrado1.calcularArea()}')
print(f'Calculo del area cuadrado: {cuadrado1.area()}')
print(cuadrado1)
print(f'Calculo del area rectangulo: {rectangulo1.area()}')
print(rectangulo1)

# #MRO - Method Resolution Order
# print(Cuadrado.mro())