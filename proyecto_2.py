from typing import List


def user_numero_entero() -> int:
    """Pone al User en un bucle del cual solo puede salir ingresando un número.
    
        numero_user -- str -- Le pide al usuario ingresar un número
        
        Muestra un mensaje de alerta, por sí el usuario no ingreso un número
    
    Retorna un variable a la cual se le asigno un entero.
    
    """
    while True:
        numero_user: str = input("Ingresa el número: ")
        if numero_user.isdigit():
            break
        else:
            print("Por favor ingresa un número")

    return int(numero_user)

def conversion_binario(numero: int) -> List:
    """En un bucle añade a la lista los residuos y el cociente de la división final.
    
        numero   -- int  -- Parámetro. Se divide entre 2, en cada vuelta del ciclo
        binario  -- list -- Vacia. Recibe los residuos y el cociente final de la división
        residuo  -- int  -- Es el residuo de la división con el número
        cociente -- int  -- Es el cociente de la división con el número
    
    Retorna una lista al revés, de los residuos y el cociente agregado en el bucle while.
    
    """
    
    binario : List = []
    while True:
        residuo: int = numero % 2
        cociente: int = numero // 2
        if residuo == 0:
            binario.append(residuo)
        elif residuo == 1:
            binario.append(residuo)
        if numero == 1 or numero == 2:
            binario.append(cociente)
            break
        
        numero = numero // 2
        
    binario.reverse()
    return binario

def mostrar_binario(binario: List) -> str:
    """Convierte binario de tipo lista a string y lo asigna a show_binario.
    
        show_binario -- str -- Nos muestra el resultado final en string
    
    Nos devuelve show_binario en formato string.
    
    """
    show_binario: str = "".join(map(str, binario))
    return show_binario
    

def run():
    """Nos muestra el menu de inicio y la secuencia del programa.
    
        numero       -- int  -- Se le asigna un número elegido por el User
        binario      -- list -- Se le asigna una lista, resultado de la conversión
        show_binario -- str  -- Se le asigna binario pero en formato string

    """
    menu = """
        Bienvenido! Este es un conversor de numeros enteros a binarios
        ⬇️           ⬇️           ⬇️           ⬇️           ⬇️
    """
    print(menu)
    numero: int = user_numero_entero()
    binario: List = conversion_binario(numero)
    show_binario: str = mostrar_binario(binario)
    print("Este es el resultado ==> ", show_binario)

if __name__ == "__main__":
    run()