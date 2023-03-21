import time
import generador
import os
from actores import Jugador, Enemigo, Bala
import random

if __name__=='__main__':

    generadorDeEscenarios = generador.GeneradorDeEscenarios()
    jugador = Jugador(columna=4)
    enemigo = Enemigo(columna=5)
    balaEnemiga = Bala(enemigo.x, enemigo.y+1)
    balaJugador = Bala(jugador.x, jugador.y-1)

    while True:
        os.system("clear")
        escenario = generadorDeEscenarios.generarEscenario()
        jugador.pintar(escenario)
        enemigo.pintar(escenario)

        if (balaJugador.estaEnEspera() == True):
            decision = random.choice([True, True, True, False])
            if (decision == True):
                balaJugador.disparar(jugador, -1)
        if (balaJugador.estaEnEspera() == False):
            balaJugador.pintar(escenario)

        if (balaEnemiga.estaEnEspera() == True):
            decision = random.choice([True, False])
            if(decision == True):
                balaEnemiga.disparar(enemigo, 1)
        if(balaEnemiga.estaEnEspera() == False):
            balaEnemiga.pintar(escenario)

        #Dibujar Escena
        for fila in escenario:
            for columna in fila:
                print(columna, end='')
            print()

        # La bala jugador esta en posicion enemiga
        # La bala enemiga esta en posicion jugador
        # Empate
        if(balaJugador.x == enemigo.x and balaJugador.y == enemigo.y and balaJugador.x == enemigo.x and balaJugador.y == enemigo.y):
            print("Fin del Juego")
            input("Has empatado")

        # La bala enemiga esta en posicion jugador
        # DERROTA
        elif(balaEnemiga.x == jugador.x and balaEnemiga.y == jugador.y):
            print("Fin del Juego")
            input("Has perdido!!!")

        # La bala jugador esta en posicion enemiga
        # VICTORIA
        elif(balaJugador.x == enemigo.x and balaJugador.y == enemigo.y):
            print("Fin del Juego")
            input("Has ganado!!!")

        time.sleep(0.0003)
        jugador.mover()
        enemigo.mover()
        balaEnemiga.mover()
        balaJugador.mover()
