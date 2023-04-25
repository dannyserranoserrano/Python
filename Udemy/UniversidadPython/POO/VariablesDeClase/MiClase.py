class MiClase:

    variablesClase = 'Valor variable clase'

    def __init__(self, variableInstancia):
        self.variableInstancia = variableInstancia

    @staticmethod  #No recibe parametros extra de nuestras clases
    def metodoEstatico():
        print(MiClase.variablesClase)

    # MiClase.metodoEstatico()

    @classmethod #Si recibe parametros extra de la clase
    def metodoClase(cls):
        print(cls.variablesClase)

    def metodoInstancia(self):
        self.metodoClase()
        self.metodoEstatico()
        print(self.variablesClase)
        print(self.variableInstancia)

MiClase.metodoClase()
miObjeto1 = MiClase('variableInstanciaJaja')
miObjeto1.metodoClase()
miObjeto1.metodoInstancia()



# print(MiClase.variablesClase)
# miClase = MiClase('Valor variable instancia')
# print(miClase.variableInstancia)
# print(miClase.variablesClase)
#
# MiClase.variablesClase2 = 'Valor variable clase 2' #Variable al vuelo
#
# miClase2 = MiClase('Otro valor de variable instancia')
# print(miClase2.variableInstancia)
# print(miClase2.variablesClase)
# print(MiClase.variablesClase2)
# print(miClase.variablesClase2)
# print(miClase2.variablesClase2)