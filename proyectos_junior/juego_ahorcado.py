from typing import List, Dict
import random
import os

def read_select(path) -> str:
    """Lee el archivo path. Añade todos los datos en una lista. Y elegi solo un dato.
    
        lista   -- list -- ListComprehension. Añade todo los datos en una lista
        
    Retorna un dato al azar de la lista    
    
    """
    with open(path, "r", encoding="utf-8") as file:
        lista: List = [i.upper().strip() for i in file]
        return random.choice(lista)

def complete_hanged(word: str) -> str:
    """Pide al usuario una letra, verifica sí esta dentro de word_lista y limpia la terminal.
        
        word          -- str  -- Parametro. Es la palabra al azar
        word_list     -- list -- Almacena en una lista las letras de word
        body_list     -- list -- Convierte todas letras en '-' para mostrarlos al jugador
        body_string   -- str  -- Muestra en pantalla '-', se reemplaza por la letra del usuario
        user_letter   -- str  -- La letra que ingresa el usuario
        enumerated    -- dict -- Un diccionario con posición y valor(key, value)
    
    Retorna un mensaje de agradecimiento tipo string para el Jugador.
    
    """
    word_list: List = [letter for letter in word]
    body_list: List = list(map(lambda x: "-", word_list))
    while True:
        print("Adivina la palabra!")
        body_string: str = " ".join(map(str, body_list))
        print(body_string)
        user_letter: str = input("Ingresa una letra: ").upper()
        if user_letter in word_list:
            enumerated: Dict = {key: value for key, value in enumerate(word_list)}
            for letter in enumerated:
                if enumerated[letter] == user_letter:
                    body_list.pop(letter)
                    body_list.insert(letter, user_letter)
                    os.system("clear")
        else:
            os.system("clear")
            continue
        if word_list == body_list:
            print(f"¡Ganaste! La palabra era {word}")
            break
    
    return "Bien hecho, Gracias por jugar este Juego😊"

def run():
    """
    
    """
    menu = """
        Bienvenido al juego clásico del Ahorcado📝
        Espero sea de tu agrado y que te diviertas mucho
        ⬇️       ⬇️       ⬇️       ⬇️       ⬇️
    """
    print(menu)
    select = read_select("./data.txt")
    message = complete_hanged(select)
    print(message)
    
if __name__ == "__main__":
    run()