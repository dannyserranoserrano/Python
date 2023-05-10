from POO.PolimorfismoEnPython.Empleado import Empleado
from POO.PolimorfismoEnPython.Gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())

empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Carla', 6000, 'Sistemas')
imprimir_detalles(gerente)