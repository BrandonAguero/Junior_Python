def convert_binary(user, numero):
    while user >= 2:
        if user % 2 == 0:
            numero.append(user % 2)
            user = user // 2
            if user // 2 == 1:
                numero.append(user // 2)
            continue
        elif user % 2 == 1:
            numero.append(user % 2)
            user = user // 2
            if user // 2 == 1:
                numero.append(user // 2) 
    return numero


def run():
    print("Cambios en SSH")
    menu = """
        Bienvenido a mi conversor de números
        te transformo números deciamles a números 
        binarios. Welcome Users
    """
    print(menu)
    user = input("Ingresa un número: ")
    user = user.strip()
    if user.isdigit() == True:
        user = int(user)
        numero = []
        numero = convert_binary(user, numero)
        numero.reverse()
        result = "".join(map(str, numero))
        print(f"La conversion de {user} a binario es {result}")
    else:
        print("Ingrese solo números!")

if __name__ == "__main__":
    run()
