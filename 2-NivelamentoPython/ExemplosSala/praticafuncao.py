#pratica1 - funcoes
#Crie um programa que represente o gerenciamente de uma pequena loja. O programa deverá ser capaz de:
# - Listar e adicionar as vendas diárias, - Exibir o valor total de vendas, - exibir a média de vendas, - exibir a maior venda

def menu():
        print("\nGerenciamento de Vendas")
        print("1. Adicionar venda")
        print("2. Listar vendas")
        print("3. Exibir valor total de vendas")
        print("4. Exibir média de vendas")
        print("5. Exibir maior venda")
        print("6. Sair")


vendas_diarias = []

def adicionar_venda(vendas_diarias, valor):

    vendas_diarias.append(valor)

def listar_vendas(vendas_diarias):

    if not vendas_diarias:
        print("Nenhuma venda registrada.")
        return
    
    print("Vendas diárias:")
    for i, venda in enumerate(vendas_diarias, start=1):
        print(f"{i}. R$ {venda:.2f}")

def total_vendas(vendas_diarias):

    total = sum(vendas_diarias)
    print(f"Valor total de vendas: R$ {total:.2f}")

def media_vendas(vendas_diarias):

    if not vendas_diarias:
        print("Nenhuma venda registrada.")
        return
    
    media = sum(vendas_diarias) / len(vendas_diarias)
    print(f"Média de vendas: R$ {media:.2f}")

def maior_venda(vendas_diarias):

    if not vendas_diarias:
        print("Nenhuma venda registrada.")
        return
    
    maior = max(vendas_diarias)
    print(f"Maior venda: R$ {maior:.2f}")


def erro():
    print("Opção inválida, por favor tente novamente.")

while True:
    menu()
    op = int(input("Digite a opção: "))

    match(op):
        case 1:
            valor = float(input("Digite o valor da venda: "))
            print(f"{adicionar_venda(vendas_diarias, valor)}")
            print("Venda adicionada com sucesso.")
        case 2:
            print(f"{listar_vendas(vendas_diarias)}")
        case 3:
            print(f"{total_vendas(vendas_diarias)}")
        case 4:
            print(f"{media_vendas(vendas_diarias)}")
        case 5:
            print(f"{maior_venda(vendas_diarias)}")
        case 6:
            print("Saindo do programa.")
            break
        case _:
            erro()

    


    