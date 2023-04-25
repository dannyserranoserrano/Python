# from Cuadrado import Cuadrado
from EjercicioHerenciaMultiple import *

#No se puede instanciar una clase abstracta
#figura = FiguraGeometrica()


print('Creacion Objeto Cuadrado'.center(50, '-'))
# print(f'Calculo del area cuadrado: {cuadrado1.calcularArea()}')
cuadrado1 = Cuadrado(lado=5, color='rojo')
print(f'Calculo del area cuadrado: {cuadrado1.area()}')
print(cuadrado1)

rectangulo1 = Rectangulo(alto=5, ancho=6, color='azul')
print('Creacion Objeto Rectangulo'.center(50, '-'))
print(f'Calculo del area rectangulo: {rectangulo1.area()}')
print(rectangulo1)

# #MRO - Method Resolution Order
print(Cuadrado.mro())