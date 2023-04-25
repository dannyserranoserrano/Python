# Ejercicio Crear Rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calculoArea(self):
        return self.base * self.altura


base = float(input("Proporciona la base: "))
altura = float(input("Proporciona la altura: "))
rectangulo1 = Rectangulo(base, altura)
print(f'Area de Rectangulo: {rectangulo1.calculoArea()}')


# Ejercicio Crear Cubo
class Cubo:
    def __init__(self, anchoX, fondoY, altoZ):
        self.anchoX = anchoX
        self.fondoY = fondoY
        self.altoZ = altoZ

    def calculoVolumen(self):
        return self.anchoX * self.fondoY * self.altoZ


anchoX = float(input("Proporciona el Ancho(Eje X): "))
fondoY = float(input("Proporciona el Fondo(Eje Y): "))
altoY = float(input("Proporciona el Alto(Eje Z): "))
cubo1 = Cubo(anchoX, fondoY, altoY)
print(f'El volumen del cubo es: {cubo1.calculoVolumen()}')
