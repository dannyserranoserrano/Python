class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad

persona1 = Persona('Juan', 30)
persona2 = Persona('Carlos', 25)

print(persona1.nombre + persona2.nombre)
print(persona1.edad - persona2.edad)

# obj1 + obj2