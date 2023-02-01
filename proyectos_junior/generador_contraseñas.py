import secrets
import string
from typing import Tuple, Dict
import os
# letters: str = string.ascii_letters
# digits: str = string.digits
# caracteres: str = string.punctuation

def caracteres_disponibles():
    letter: str = string.ascii_letters
    digits: str = string.digits
    caracteres: str = string.punctuation
    return letter, digits, caracteres


def tamaño_contraseña():
    """Presentación. Pregunta al usuario cuál será el tamaño de su contraseña.

        respuestas   -- tuple -- Tiene las respuestas validas 
        menu         -- str   -- Tiene asignado una presentación
        tamaño_one   -- str   -- Pregunta al User sí ese es el tamaño adecuado
        tamaño_two   -- str   -- Pregunta al User sí ese es el tamaño adecuado
        tamaño_three -- str   -- Pregunta al User sí ese es el tamaño adecuado
        reinicio     -- str   -- Pregunta al User sí quiere volver al inicio
    
    Retorna el tamaño de la contraseña, que elegió el usuario.
    
    """
    respuestas: Tuple = ("yes", "no")
    menu: str = """
        ✨✨✨Bienvenido al mejor generador de contraseñas✨✨✨
        Tienes las siguientes opciones:
            Tamaño:
                - 08 Caracteres
                - 12 Caracteres
                - 16 Caracteres
            Tipo:
                - Letras 
                - Numeros
                - Caracteres Especiales
        Para poder elegir entre estas opciones tendras que solo responder:
            - Yes 
            - No
    """
    print(menu)
    while True:
        tamaño_one: str = input("Usted desea 8 caracteres para su contraseña?: ").lower().strip()
        if tamaño_one.isdigit() or not tamaño_one in respuestas:
            print('Por favor solo ingresa estas opciones "Yes" or "No"')
            continue
        elif tamaño_one == "yes" and tamaño_one.isalpha():
            return 8

        if tamaño_one == "no":
            break
    
    while True:
        tamaño_two: str = input("Usted desea 12 caracteres para su contraseña?: ").lower().strip()
        if tamaño_two.isdigit() or not tamaño_two in respuestas:
            print('Por favor solo ingresa estas opciones "Yes" or "No"')
            continue
        elif tamaño_two == "yes" and tamaño_two.isalpha():
            return 12
        
        if tamaño_two == "no":
            break
    
    while True:
        tamaño_three: str = input("Usted desea 16 caracteres para su contraseña?: ").lower().strip()
        if tamaño_three.isdigit() or not tamaño_three in respuestas:
            print('Por favor solo ingresa estas opciones "Yes" or "No"')
            continue
        elif tamaño_three == "yes" and tamaño_three.isalpha():
            return 16
        
        if tamaño_three == "no":
            print('Por favor tienes que elegir el tamaño de tu contraseña')
            while True:
                reinicio: str = input("Quieres volver a empezar? ").lower().strip()
                if reinicio.isdigit() or not reinicio in respuestas:
                    print('Por favor solo ingresa estas opciones "Yes" or "No"')
                    continue
                elif reinicio == "no":
                    print("Por favor eliga una opción")
                    break
                elif reinicio == "yes":
                    os.system("clear")
                    return tamaño_contraseña()
                
def tipo_contraseña():
    respuestas: Tuple = ("yes", "no")
    tipo: Dict = {
        "letras": 0,
        "numeros": 0,
        "caracteres": 0
    }
    while True:
        tipo_one: str = input("Usted desea letras para su contraseña?: ").lower().strip()
        if tipo_one.isdigit() or not tipo_one in respuestas:
            print('Por favor solo ingresa estas opciones "Yes" or "No"')
            continue
        elif tipo_one == "yes" and tipo_one.isalpha():
            tipo["letras"] = 1
            break

        if tipo_one == "no":
            break
    
    while True:
        tipo_two: str = input("Usted números para su contraseña?: ").lower().strip()
        if tipo_two.isdigit() or not tipo_two in respuestas:
            print('Por favor solo ingresa estas opciones "Yes" or "No"')
            continue
        elif tipo_two == "yes" and tipo_two.isalpha():
            tipo["numeros"] = 1
            break
        
        if tipo_two == "no":
            break
    
    while True:
        tipo_three: str = input("Usted desea caracteres especiales para su contraseña?: ").lower().strip()
        if tipo_three.isdigit() or not tipo_three in respuestas:
            print('Por favor solo ingresa estas opciones "Yes" or "No"')
            continue
        elif tipo_three == "yes" and tipo_three.isalpha():
            tipo["caracteres"] = 1
            break
        
        if tipo_three == "no":
            print('Por favor tienes que elegir el algún tipo de contraseña')
            while True:
                reinicio: str = input("Quieres volver a empezar? ").lower().strip()
                if reinicio.isdigit() or not reinicio in respuestas:
                    print('Por favor solo ingresa estas opciones "Yes" or "No"')
                    continue
                elif reinicio == "no":
                    print("Por favor eliga una opción")
                    break
                elif reinicio == "yes":
                    os.system("clear")
                    return tipo_contraseña()
    
    return tipo

def generando_contraseña(tamaño, tipo):
    pass


def run():
    tamaño: int = tamaño_contraseña()
    tipo: str = tipo_contraseña()
    contraseña: str = generando_contraseña(tamaño, tipo)
    print(f"Esta es tu contraseña {contraseña}")
    print("Gracias por su preferencia🥰")
if __name__ == "__main__":
    run()