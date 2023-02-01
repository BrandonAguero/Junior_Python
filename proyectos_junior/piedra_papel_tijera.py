import random
from typing import Tuple

def contador_rondas():
    """Asigna valores enteros a las variables y las retorna.

        rondas    -- int -- Es el número de rondas del Juego 
        victorias -- int -- Es el número de victorias del usuario
        derrotas  -- int -- Es el número de derrotas del usuario   

    Retorna las variables con sus valores asignados.
    
    """
    rondas: int = 1
    victorias: int = 0
    derrotas: int = 0
    return rondas, victorias, derrotas

def show_user_computer():
    """Elige una opcion al azar para computer y pregunta su opción al user.
    
        options     -- tupla -- Establece las opciones disponibles
        computer    --  str  -- Pregunta al usuario su opción
        user        --  str  -- Elige al azar una opción disponible de options
        menu_eror   --  str  -- Muestra un menú de error, por sí el usuario ingresa una opción incorrecta
    
    Retorna las variables con sus valores asignados
    
    """
    options: Tuple = ("Piedra", "Papel", "Tijera")
    while True:
        menu_error: str = """
            Por favor ingresa solo estas opciones:
                - Piedra 🪨
                - Papel  🧻
                - Tijera ✂️
        """
        user: str = input("Ingresa la opción que elegiste: ").capitalize()
        if user.isalpha() and user in options:
            break
        elif user.isalpha() != True or user not in options:
            print(menu_error)
    computer: str = random.choice(options)
    return user, computer

def who_winner(user: str, computer: str, victorias: int, derrotas: int):
    """Verifica quién ganó, perdió o sí es un empate. Cuenta las victorias y derrotas.
    
        user      -- str -- Es comparado con computer. Para ver el resultado de las comparaciónes
        computer  -- str -- Es comparado con user. Para ver el resultado de las comparaciónes
        victorias -- int -- Suma una unidad. Para las victorias de user
        derrotas  -- int -- Suma una unidad. Para las victorias de computer

        Muestra quién ganó, perdió o sí fue un empate.
        
    Retorna el número de victorias y derrotas.
    
    """    
    if user == computer:
        print("Esta ronda es un EMPATE!!!")
        victorias += 0
        derrotas += 0
    elif user == "Piedra":
        if computer == "Papel":
            print("El ganador de esta ronda es la COMPUTADORA!!!")
            derrotas += 1
        else:
            print("El ganador de esta ronda es el USUARIO!!!")
            victorias += 1
    elif user == "Papel":
        if computer == "Tijera":
            print("El ganador de esta ronda es la COMPUTADORA!!!")
            derrotas += 1
        else:
            print("El ganador de esta ronda es el USUARIO!!!")
            victorias += 1
    elif user == "Tijera":
        if computer == "Piedra":
            print("El ganador de esta ronda es la COMPUTADORA!!!")
            derrotas += 1
        else:
            print("El ganador de esta ronda es el USUARIO!!!")
            victorias += 1
    else:
        pass
    
    return victorias, derrotas

def delimitador_rondas(victorias: int, derrotas: int):
    """Verifica sí las victorias y derrotas son iguales, para finalizar el ciclo y mostrar el resultado
    
        victorias  -- int -- Representa las victorias de user.
        derrotas   -- int -- Representa las victorias de computer.

        Muestras las victorias y derrotas del usuario.
    
    Retorna la función exit() para finalizar el ciclo
    
    """
    if victorias == 3:
        if derrotas == 3:
            print(f"Las victorias de User ==> {victorias} ")
            print(f"Las victorias de Computer ==> {derrotas}")
            print("🔥Esto fue un ROTUNDO EMPATE!!!🔥")
            return exit()
    if victorias == 3:
        print(f"User ganó {victorias} veces")
        print(f"Computer ganó {derrotas} veces")
        print("🧍 Gana el USUARIO!!!🕺")
        return exit()
    if derrotas == 3:
        print(f"Computer ganó {derrotas} veces")
        print(f"User ganó {victorias} veces")
        print("🤖Gana la COMPUTADORA!!!🤖")
        return exit()

def run():
    """Nos muestra la secuencia del juego.
    
        menu    -- str -- Es el menu de bienvenida del juego
        rondas  -- int -- Cuenta las rondas del juego
        
    """
    
    rondas, victorias, derrotas = contador_rondas()
    menu: str = """
        ✊✋✌️ Bienvenido al juego clásico de Piedra, Papel y Tijera✊✋✌️
        A continuación alige entre estas opciones:
            - Piedra 🪨
            - Papel  🧻
            - Tijera ✂️
    """
    print(menu)
    while True:
        print("*" * 5, f"RONDA {rondas}", "*" * 5)
        user, computer = show_user_computer()
        victorias, derrotas = who_winner(user, computer, victorias, derrotas)
        delimitador_rondas(victorias, derrotas)
        rondas += 1

if __name__ == "__main__":
    run()