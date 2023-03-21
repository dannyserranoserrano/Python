import time

while(True):
    tiempo = input("Tiempo del contador (salir escribiendo 'salir'): ")
    if(tiempo == "salir"):
        exit()
    elif(tiempo.isnumeric() == False):
        print("No pusiste un numero!!!")
    else:
        tiempoEnValorEntero = int(tiempo)
        print("Esperando " + tiempo + " segundos")  # Concatena
        print("Esperando", tiempoEnValorEntero, "segundos")  # Ejecuta los 3
        time.sleep(int(tiempo))