def obtenerLineasArchivo(nombre):
    try:
        lineasDeArchivo = open(nombre, "r").read().splitlines()
        return lineasDeArchivo
    except OSError:
        print("No se ha podido abrir archivo", nombre)
        return -1
    except:
        print("Cualquier otro tipo de fallo ocurrio al abrir")
        return -2
    finally:
        print("Operacion de apertura finalizada")

def escribirLineasArchivo(nombre, lineas):
    try:
        archivo = open(nombre, 'w')
        resultado = ""
        for linea in lineas:
            try:
                operadores = linea.split('+')
                val1, val2 = operadores
                #Es lo mismo que lo anterior, solo que lo esta descomponiendo:
                    #val1 = operadores[0]
                    #val2 = operadores[1]
                val1 = float(val1)
                val2 = float(val2)
                suma = val1+val2
                sumaTexto = str(suma)
                linea = linea + "=" + sumaTexto
                resultado = resultado + linea + "\n"
            except:
                if(linea.find("=")):
                    resultado = resultado + linea + "\n"
                else:
                    print("No se han podido realizar alguna de las sumas")
        archivo.write(resultado)


    except:
        print("No se puede escribir en el archivo")
    finally:
        print("Operacion  de escritura finalizada")

lineas = obtenerLineasArchivo('texto.txt')

if (lineas != -1 and lineas != -2):
    escribirLineasArchivo("texto.txt", lineas)
