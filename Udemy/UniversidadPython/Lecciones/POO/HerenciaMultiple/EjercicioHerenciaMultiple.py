#ABC = abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        if self._validarValor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo alto: {alto}')
        if self._validarValor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print (f'Valor erroneo alto: {ancho}')


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
        if self._validarValor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo ancho: {alto}')

    @ancho.setter
    def ancho(self, ancho):
        if self._validarValor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'El Alto es: {self.alto} y el Ancho es: {self.ancho}'

    def _validarValor(self, valor):
        return True if 0 < valor < 10 else False
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
        return f'CUADRADO: {self.color}, {self.alto}, {self.ancho}, {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'RECTANGULO: {self.color}, {self.alto}, {self.ancho}, {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'

