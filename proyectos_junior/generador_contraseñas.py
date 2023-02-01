import secrets
import string
from typing import Tuple
import os

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
    """Pregunta al usuario que tipo de contraseña quiere se le genere.
    
        respuestas  -- tuple -- Tiene solo las respuestas aceptables 
        tipo        -- dict  -- Almacena 0 para False(no) y 1 para True(si) 
        tipo_one    -- str   -- Pregunta al usuario si quiere letras en su contraseña
        tipo_two    -- str   -- Pregunta al usuario si quiere numeros en su contraseña
        tipo_three  -- str   -- Pregunta al usuario si quiere caracteres especiales en su contraseña
        reinicio    -- str   -- Pregunta si quiere empezar nuevamente a elegir su tipo de contraseña
        
    Retorna una lista con 0 y 1, donde el 0 representa False(no) y el 1 representa True(si).
    
    """
    respuestas: Tuple = ("yes", "no")
    tipo: list = []
    while True:
        tipo_one: str = input("Usted desea letras para su contraseña?: ").lower().strip()
        if tipo_one.isdigit() or not tipo_one in respuestas:
            print('Por favor solo ingresa estas opciones "Yes" or "No"')
            continue
        elif tipo_one == "yes" and tipo_one.isalpha():
            tipo.append(1)
            break

        if tipo_one == "no":
            tipo.append(0)
            break
    
    while True:
        tipo_two: str = input("Usted números para su contraseña?: ").lower().strip()
        if tipo_two.isdigit() or not tipo_two in respuestas:
            print('Por favor solo ingresa estas opciones "Yes" or "No"')
            continue
        elif tipo_two == "yes" and tipo_two.isalpha():
            tipo.append(1)
            break
        
        if tipo_two == "no":
            tipo.append(0)
            break
    
    while True:
        tipo_three: str = input("Usted desea caracteres especiales para su contraseña?: ").lower().strip()
        if tipo_three.isdigit() or not tipo_three in respuestas:
            print('Por favor solo ingresa estas opciones "Yes" or "No"')
            continue
        elif tipo_three == "yes" and tipo_three.isalpha():
            tipo.append(1)
            break

        if tipo_three == "no" and tipo_one == "no" and tipo_two == "no":
            while True:
                reinicio: str = input("Quieres volver a empezar a elegir nuevamente tu tipo de contraseña? ").lower().strip()
                if reinicio.isdigit() or not reinicio in respuestas:
                    print('Por favor solo ingresa estas opciones "Yes" or "No"')
                    continue
                elif reinicio == "no":
                    print("Por favor eliga una opción")
                    break
                elif reinicio == "yes":
                    os.system("clear")
                    return tipo_contraseña()
        elif tipo_three == "no":
            tipo.append(0)
            break
    
    return tipo

def generando_contraseña(tamaño, tipo) -> str:
    """Genera la contraseña basado en el tamaño y el tipo que pida el usuario.

        tamaño              -- int  -- Parámetro, es el tamaño que pide el usuario
        tipo                -- list -- Parámetro, s el tipo de contraseña que pide el usuario
        letras              -- str  -- Todas las letras que pueden agregarse a la contraseña
        numeros             -- str  -- Todos los numeros que pueden agregarse a la contraseña
        especiales          -- str  -- Todos los caracteres especiales que pueden agregarse a la contraseña
        todos_caracteres    -- str  -- Es la concatenación de letras, numeros y especiales
        numeros_especiales  -- str  -- Es la concatenación de números y especiales
        letras_numeros      -- str  -- Es la concatenación de letras y números
        letras_especiales   -- str  -- Es la concatenación de letras y especiales 
        result_contraseña   -- str  -- Es el resultado final de la contraseña generada
        
    Retorna result_contraseña. El cuál es el resultado del generador de contraseñas
    
    """
    letras: str = string.ascii_letters
    numeros: str = string.digits
    especiales: str = string.punctuation
    todos_caracteres: str = letras + numeros + especiales
    numeros_especiales: str = numeros + especiales
    letras_numeros: str = letras + numeros
    letras_especiales: str = letras + especiales
    result_contraseña: str = ""
    if tipo[0] == 1 and tipo[1] == 1 and tipo[2] == 1:
        while len(result_contraseña) < tamaño:
            result_contraseña += "".join(map(str, secrets.choice(todos_caracteres)))
    elif tipo[0] == 0 and tipo[1] == 1 and tipo[2] == 1:
        while len(result_contraseña) < tamaño:
            result_contraseña += "".join(map(str, secrets.choice(numeros_especiales)))
    elif tipo[0] == 0 and tipo[1] == 0 and tipo[2] == 1:
        while len(result_contraseña) < tamaño:
            result_contraseña += "".join(map(str, secrets.choice(especiales)))
    elif tipo[0] == 1 and tipo[1] == 1 and tipo[2] == 0:
        while len(result_contraseña) < tamaño:
            result_contraseña += "".join(map(str, secrets.choice(letras_numeros)))
    elif tipo[0] == 1 and tipo[1] == 0 and tipo[2] == 0:
        while len(result_contraseña) < tamaño:
            result_contraseña += "".join(map(str, secrets.choice(letras)))
    elif tipo[0] == 1 and tipo[1] == 0 and tipo[2] == 1:
        while len(result_contraseña) < tamaño:
            result_contraseña += "".join(map(str, secrets.choice(letras_especiales)))
    elif tipo[0] == 0 and tipo[1] == 1 and tipo[2] == 0:
        while len(result_contraseña) < tamaño:
            result_contraseña += "".join(map(str, secrets.choice(numeros)))
    
    return result_contraseña

def run():
    """Nos muestra la secuencia del 'Generador de Contraseñas'.

        tamaño      -- int -- Se le asigna el tamaño de contraseña que el usuario eligió  
        tipo        -- str -- Se le asigna el tipo de contraseña que el usuario eligió
        contraseña  -- str -- Se le asigna la contraseña que se genero en base a las peticiones del usuario
        
    
    """
    tamaño: int = tamaño_contraseña()
    tipo: str = tipo_contraseña()
    contraseña: str = generando_contraseña(tamaño, tipo)
    print(f"Esta es tu contraseña ==> {contraseña}")
    print("Gracias por su preferencia🥰")

if __name__ == "__main__":
    run()