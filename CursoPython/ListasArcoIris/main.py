listaDePalabras = ["Hola", "como", "estas", "hoy", "es", "un", "gran", "dia", "para", "salir"]

RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
END = "\033[0m"
listaDeColores = [RED, GREEN, BLUE]

while(len(listaDePalabras)>0):
    colorEscogido = listaDeColores.pop(0)
    elemento = listaDePalabras.pop(0)
    print(colorEscogido + elemento, end=" ")
    listaDeColores.append(colorEscogido)

print(END)
print("Hemos acabado")

