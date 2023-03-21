import copy

if __name__=='__main__':
    print("Este archivo no se puede ejecutar tal cual, debes importarlo en main.py")
    print("En este archivo declaramos la clase GeneradorDeEscenarios() que contiene la funcion generarEscenario()")

class GeneradorDeEscenarios():
    filaConParedes = list("####################")
    filaConLateralesDeParedes = list("#                  #")
    escenario = [
        list(filaConParedes),
        list(filaConLateralesDeParedes),
        list(filaConLateralesDeParedes),
        list(filaConLateralesDeParedes),
        list(filaConLateralesDeParedes),
        list(filaConLateralesDeParedes),
        list(filaConLateralesDeParedes),
        list(filaConLateralesDeParedes),
        list(filaConLateralesDeParedes),
        list(filaConParedes)
    ]

    def generarEscenario(self):
        return copy.deepcopy(self.escenario)