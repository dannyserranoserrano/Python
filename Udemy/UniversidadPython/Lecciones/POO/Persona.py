# Creacion de Clase
class Persona:
    def __init__(self, nombre, apellido, edad, *args, **kwards):  # Tambien se pueden insertar tuplas o diccionarios
        # self se puede cambiar por otra palabra, en Javascript u otros lenguajes es this
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwards = kwards

    # Creacion de Metodo
    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.args} {self.kwards}')

    # Metodo destructor de objetos
    def __del__(self):
        print(f'Persona: {self.nombre} {self.apellido}')

if __name__ == "__main__":  # Sirve para que solo se ejecute ese codigo si lo ejecutamos desde el archivo Persona.
# PRINTS
    persona1 = Persona('Danny', 'Serrano', 40, '4433554433', 2, 3, 4, m='manzana', p='pera',
                       l='limon')  # Creacion y asignacion de una persona
    persona1.mostrarDetalle()  # Llamada al metodo
    # print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
    # Persona.mostrarDetalle(persona1)
    # persona1.telefono = "659547749"  # Agregar nuevos atributos(Referenciado solo a persona 1)

    # persona2 = Persona('Carlos', 'Gomez', 30)  # Creacion y asignacion de una persona
    # persona2.mostrarDetalle()  # Llamada al metodo
    # # print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
    # Persona.mostrarDetalle(persona2)

    print(__name__)  # Muestra el modulo que se esta ejecutando

    # Modificar datos
    # persona1.nombre = 'Juan Carlos'
    # persona1.apellido = 'Perez' #Modificar datos
    # persona1.edad = 25 #Modificar datos
    # print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
