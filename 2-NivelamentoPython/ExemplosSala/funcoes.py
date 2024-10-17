#exemplo1


def menu():
    print("****MENU*******")
    print("1 - Exibir Hello World\n2 - Exibir Olá Mundo")


def ingles():
    print("Hello World")

def portugues():
    print("Olá Mundo")

while True:
    menu()
    op = int(input("Digite a opção: "))

    match(op):
        case 1:
            ingles()
        case 2:
            portugues()
        case _:
            print("Opção Inválida")


