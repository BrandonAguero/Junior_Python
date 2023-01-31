import random
from typing import Tuple

def contador_rondas():
    numero_rondas: int = 1
    victorias: int = 0
    derrotas: int = 0
    return numero_rondas, victorias, derrotas

def show_user_computer():
    options: Tuple = ("Piedra", "Papel", "Tijera")
    user: str = input("Ingresa la opcion que elegiste: ").capitalize()
    computer: str = random.choice(options)
    return user, computer

def who_winner(user: str, computer: str, victorias: int, perdidas: int):
        if user == computer:
            print("Esta ronda es un EMPATE!!!")
            victorias += 1
            perdidas += 1
        elif user == "Piedra":
            if computer == "Papel":
                print("El ganador de esta ronda es la COMPUTADORA!!!")
                perdidas += 1
            else:
                print("El ganador de esta ronda es el USUARIO!!!")
                victorias += 1
        elif user == "Papel":
            if computer == "Tijera":
                print("El ganador de esta ronda es la COMPUTADORA!!!")
                perdidas += 1
            else:
                print("El ganador de esta ronda es el USUARIO!!!")
                victorias += 1
        elif user == "Tijera":
            if computer == "Piedra":
                print("El ganador de esta ronda es la COMPUTADORA!!!")
                perdidas += 1
            else:
                print("El ganador de esta ronda es el USUARIO!!!")
                victorias += 1
        else:
            print("Por favor ingresa una opcion CORRECTA!!!")
        return victorias, perdidas

def delimitador_rondas(victorias: int, derrotas: int):
    if victorias == 3:
        if derrotas == 3:
            print(f"Ganaste {victorias} veces")
            print(f"Perdiste {derrotas} veces")
            print("Esto fue un ROTUNDO EMPATE!!!")
            return exit()
    if victorias == 3:
        print(f"Ganaste {victorias} veces")
        print(f"Perdiste {derrotas} veces")
        print("Gana el USUARIO!!!")
        return exit()
    if derrotas == 3:
        print(f"Ganaste {victorias} veces")
        print(f"Perdiste {derrotas} veces")
        print("Gana la COMPUTADORA!!!")
        return exit()

def run():
    numero_rondas, victorias, derrotas = contador_rondas()
    menu: str = """
        Bienvenido al juego clásico de Piedra, Papel y Tijera
        A continuación alige entre las opciones: 
    """
    print(menu)
    while True:
        print("*" * 5, f"RONDA {numero_rondas}", "*" * 5)
        user, computer = show_user_computer()
        print("Usuario ==>", user)
        print("Computadora ==>", computer)
        victorias, derrotas = who_winner(user, computer, victorias, derrotas)
        delimitador_rondas(victorias, derrotas)
        numero_rondas += 1

if __name__ == "__main__":
    run()