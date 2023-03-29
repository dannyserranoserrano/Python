#Creacion de Clase
class Persona:
    def __init__(self, nombre, apellido, edad):
#self se puede cambiar por otra palabra, en Javascript u otros lenguajes es this
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
#Creacion de Metodo
    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

#PRINTS
persona1 = Persona('Danny', 'Serrano', 40) #Creacion y asignacion de una persona
persona1.mostrarDetalle() #Llamada al metodo
#print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
Persona.mostrarDetalle(persona1)
persona1.telefono = "659547749" #Agregar nuevos atributos(Referenciado solo a persona 1)

persona2 = Persona('Carlos', 'Gomez', 30) #Creacion y asignacion de una persona
persona2.mostrarDetalle() #Llamada al metodo
#print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
Persona.mostrarDetalle(persona2)

# Modificar datos
#persona1.nombre = 'Juan Carlos'
#persona1.apellido = 'Perez' #Modificar datos
#persona1.edad = 25 #Modificar datos
#print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')



