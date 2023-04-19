class Vehiculo:
    def __init__(self, marca: str, color: str, ruedas: int):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Marca: {self.marca}, Color: {self.color}, Ruedas(Pulgadas): {self.ruedas}'


class Coche(Vehiculo):
    def __init__(self, marca: str, color: str, ruedas: int, velocidad: int):
        super().__init__(marca, color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'COCHE {super().__str__()} , Velocidad(km/h): {self.velocidad}'


class Bicicleta(Vehiculo):
    def __init__(self, marca: str, color: str, ruedas: int, tipo: str):
        super().__init__(marca, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'BICICLETA {super().__str__()} , Tipo: {self.tipo}'


coche1 = Coche("Audi", "Blanco", 18, 240)
print(coche1)
bicicleta1 = Bicicleta("Scott", "Azul", 29, "MTB")
print(bicicleta1)
