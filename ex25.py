"""
Programa que mostra um menu com opções e registra jogos usando laço de iteração, dicionário e lista
game = lista que armazena  o dicionário com nome e videogame do jogo;
choice = escolha de opção do menu vinda do usuário
games = dicionário que armazena par chave-vale nome e videogame.
"""


def register_item(name_file):
    try:
        a = open(name_file, "at")
    except:
        print("Error trying to open file")
    else:
        print("-" * 30)
        name = input("Name's game: ")
        videogame = input("Belonging video game: ")
        a.write(f"{name} ; {videogame}")
    finally:
        a.close()


def list_items(name_file):
    print("-" * 30)
    try:
        a = open(name_file, "rt")
    except:
        print("Error to read file.")
    else:
        print(a.read())
    finally:
        a.close()
    print("-" * 30)


def valid_value():
    while True:
        try:
            print("Choose an option between 1 and 3:")
            print("1 - Register a new Item;")
            print("2 - List registered items;")
            print("3 - Exit the program.")
            choice = int(input("Answer: "))
            break
        except ValueError:
            print("Try again and enter an integer number!")
            continue
    return choice


def create_archive(archive_name):
    try:
        a = open(archive_name, "wt+")  # escrita do tipo texto + a criação do arquivo
        a.close()
    except:
        print("Archive creating error.")
    else:
        print("Archive created successfully!")


def exist_file(archive_name):
    try:
        a = open(archive_name, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


FILE_NAME = "games.txt"

if exist_file(FILE_NAME):
    print("File found in computer.")
else:
    print("nonexistent file")
    create_archive(FILE_NAME)
while True:
    option = valid_value()
    if option == 1:
        register_item(FILE_NAME)
        continue
    if option == 2:
        list_items(FILE_NAME)
        continue
    if option == 3:
        print("-" * 30)
        print("Closing the program...")
        break
