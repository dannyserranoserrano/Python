#Argumentos variables *Args
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres('Juan', 'Carla', 'Maria', 'Ernesto')
listarNombres('Laura', 'Carlos')

#Llave-Valor **kwards
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')
listarTerminos(IDE="Integrated Developement Enviroment", PK='Primary Key')
listarTerminos(DBMS="Database Management System")

#Distintos tipos de datos
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Carla', 'Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres([10, 11])
