class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    # GET (Coger)
    @property
    def alto(self):
        return self._alto

    @property
    def ancho(self):
        return self._ancho

    # SET (Establecer)
    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    def __str__(self):
        return f'El Alto es: {self.alto} y el Ancho es: {self.ancho}'


class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'El  color es: {self.color}'


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'CUADRADO: {self.color}, {self.ancho}, {self.alto}, {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'RECTANGULO: {self.color}, {self.ancho}, {self.alto}, {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'

