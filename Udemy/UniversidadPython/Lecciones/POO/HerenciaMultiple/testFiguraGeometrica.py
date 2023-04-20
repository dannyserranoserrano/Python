# from Cuadrado import Cuadrado
from EjercicioHerenciaMultiple import *

print('Creacion Objeto Cuadrado'.center(50, '-'))
# print(f'Calculo del area cuadrado: {cuadrado1.calcularArea()}')
cuadrado1 = Cuadrado(lado=5, color='rojo')
print(f'Calculo del area cuadrado: {cuadrado1.area()}')
print(cuadrado1)

rectangulo1 = Rectangulo(alto=50, ancho=6, color='azul')
print('Creacion Objeto Rectangulo'.center(50, '-'))
print(f'Calculo del area rectangulo: {rectangulo1.area()}')
print(rectangulo1)

# #MRO - Method Resolution Order
# print(Cuadrado.mro())