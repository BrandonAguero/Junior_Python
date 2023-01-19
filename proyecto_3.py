import random
import os

def read_select(path):
    with open(path, "r", encoding="utf-8") as file:
        lista = []
        for i in file:
            i = i.upper()
            lista.append(i.strip())
    select = random.choice(lista)
    return select

def complete_hanged(word):
    word_list = [letter for letter in word]
    espected_word = "".join(map(str, word_list))
    body_list = list(map(lambda x: "-", word_list))
    body_string = " ".join(map(str, body_list))
    while True:
        print("Adivina la palabra!")
        menu = """
            @@@@@X@@@@@@@@@@@@@X@@@@@@@@@@@@@@@@8 . 
            @@@X@@@@8@@X8@@X8@@@@@@8@@X8@@X88XX@8 . 
            @@@@@@88@88@88XS8@@X.@@888@888@8@88@t   
            @@@@888X . ..8 8XS 8 .. . . .  St% . .  
            @@@@@@8S .. :%8@%: .         ..S@S .   .
            @@@@8X8X .S:X8XS@.  .  . . .  .Xt% . . .
            @@88@@8Xt%t888X..    .       ..SXS  ;X8 
            @@@@@S@:;8X@8 .   .    .  .  . @%t;X@:88
            @@@@88@@@8St.   .   .      . S@@:X8@:S .
            @@@@@8XX::.  .    .   . . . 88   S8S .  
            @@@@@@8@ . .  .     .     . 8   ...X .  
            @@@@8@8X .     . .     .   . @.   8.  . 
            @@888@8X .  .      .     .  . ;;%X .    
            @@@8@S8X     .  .    . .    .  8 X8 . . 
            @@@@888S . .      .       .. %:@.t8S .  
            @@@@@@8X .   . .    .  .   .;X8@.SXtS   
            @@@@@X8X   .     .   .   .. ;.8.: t.  . 
            @@@@8@8S. .   .    .    . . 8:S . 8;X . 
            @@88@@8S .  .   .     .   . t.; : XX    
            @@@8@@8X      .   .  .   .  %88X ; ;; . 
            @@@@@@8X . .    .      .   . 8.8888S.  .
            @@@@@X8X .   .     .     .   ..:%t.  .  
            @@@@888S .  .  .  .  .     .   ...      
            @@@@@@8X  .           . .    .     .  . 
            @@@@@X8X .  .    .    .     .    . .    
            @@@@888S .    .    .     .     .     .  
            @@@X8@8X  . .   .    .  .  .  .   .    .
            @@888@8S .    .   .             .   .   
            @@@8@@8X . ..  . . .. .. .. .. . . . .. 
            S;t%ttXS8@@@@88888@88888888X@@@@@@@@@@@@
        """
        print(menu)
        body_string = " ".join(map(str, body_list))
        print(body_string)
        user_letter = input("Ingresa una letra: ")
        user_letter = user_letter.upper()
        if user_letter in word_list:
            enumerated = {key: value for key, value in enumerate(word_list)}
            for letter in enumerated:
                if enumerated[letter] == user_letter:
                    body_list.pop(letter)
                    body_list.insert(letter, user_letter)
                    os.system("clear")
        else:
            os.system("clear")
            continue
        if word_list == body_list:
            print(f"¡Ganaste! La palabra era {espected_word}")
            break

def run():
    select = read_select("./data.txt")
    complete_hanged(select)

if __name__ == "__main__":
    run()