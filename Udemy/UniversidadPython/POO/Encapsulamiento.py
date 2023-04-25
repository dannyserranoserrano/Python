class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # Metodo GET
    @property  # Este decorador hace que podamos acceder al atributo mediante el metodo sin poner ()
    def nombre(self):
        print('Llamando método GET Nombre')
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    @property
    def edad(self):
        return self._edad

    # Metodo SET
    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método SET Nombre')
        self._nombre = nombre
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')


persona1 = Persona('Danny', 'Serrano', 40)
print(persona1.nombre)
persona1.nombre = 'Juan Carlos'  # Con esto ya podemos reasignar el valor de Nombre gracias a @nombre.setter.
print(persona1.nombre)
# persona1._nombre = 'Paco'  # Esto NO se debe hacer, ya que está encapsulado con_
# persona1.mostrarDetalle()  # Ejecuta ese método.
# print(persona1.nombre())  # Con esto ejecutamos el método que nos lleva a nombre (si no tuviésemos @property)
# print(persona1._nombre)  # Esto NO se debe hacer
# print(persona1.nombre)
# El atributo con _ quiere decir que no se debería acceder fuera de la clase.
# Python deja, pero no se debe. Si queremos ser más restrictivos se puede insertar __ y ahora si te lo bloquea.
# Método GET obtiene un atributo de la clase Método SET modifica un atributo a la clase
