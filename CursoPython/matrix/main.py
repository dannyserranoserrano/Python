import os
import time
import random

def limpiarPantalla():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def generarCaracter():
    # Caracteres Habituales 33 a 123
    numero = (random.randint(33, 125))
    ponerEspacio = random.choice([True, True, False])
    if(ponerEspacio):
        return " "
    elif(ponerEspacio == False):
        return chr(numero)

def generarLinea(letrasPorFila):
    linea = ""
    for posicion in range(letrasPorFila):
        linea = linea + generarCaracter()
    return linea

def generarListaDeLineas(letrasPorFila,lineas):
    listaDeLineas = []
    for linea in range(lineas):
        valorRetornado = generarLinea(letrasPorFila)
        listaDeLineas.append(valorRetornado)
    return listaDeLineas

limpiarPantalla()
letrasPorFila, lineas = os.get_terminal_size()
listaGenerada = generarListaDeLineas(letrasPorFila, lineas)
colorVerde = "\033[0;32m"
print(colorVerde)

while(True):
    for linea in listaGenerada:
        print(linea)

    ultimaLinea = listaGenerada.pop()
    listaGenerada.insert(0, ultimaLinea)
    time.sleep(0.07)