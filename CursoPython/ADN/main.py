cadenaADN = ["T","T","A", "C","G"]
cadenaARN = []
cadenaARNInvertida = []

print("Cadena Inicial ADN:")
print(cadenaADN)
#Encargado de generar ARN
for element in cadenaADN:
    if(element == "C"):
        cadenaARN.append("G")
    elif(element == "T"):
        cadenaARN.append("A")
    elif(element == "A"):
        cadenaARN.append("U")
    elif(element == "G"):
        cadenaARN.append("C")

#Encargado de mostrar ARN
print("ARN:")
print(cadenaARN)

#Encargado de mostrar ARN Reversed
longitudCadena = len(cadenaARN)
for indice in range(longitudCadena):
    elemento = cadenaARN.pop()
    cadenaARNInvertida.append(elemento)

print("Reversed ARN:")
print(cadenaARNInvertida)