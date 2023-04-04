# Prueba Persona
from Persona import Persona

# persona1 = Persona('Carla', 'Gomez', 30)
# persona1.mostrarDetalle()
#
# print(__name__)  # Muestra el modulo que se esta ejecutando

# Destructor de Objetos en Python (Creado en Persona)

print('Creacion de objetos' .center(50, '-'))
persona1 = Persona('Carla', 'Gomez', 30)
persona1.mostrarDetalle()

print('Eliminacion de objetos' .center(50, '-'))
del persona1
