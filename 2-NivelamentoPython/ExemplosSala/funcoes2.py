#exemplo2


def menu():
    print("****MENU*******")
    print("1 - SOMAR\n2 - SUBTRAIR\n3 - SAIR")


def soma(a,b):
    print(f"{a} + {b} = {a+b}")

def subtrair(a,b):
    print(f"{a} - {b} = {a-b}")

def erro():
    print("Opção Inválida")

while True:
    menu()
    op = int(input("Digite a opção: "))

    match(op):
        case 1:
            valores = input("Digite os dois valores: ").split()
            soma(int(valores[0]),int(valores[1]))
        case 2:
            valores = input("Digite os dois valores: ").split()
            subtrair(int(valores[0]),int(valores[1]))

        case 3:
            print("Saindo......")
            break
        case _:
            erro()


