def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar item")
    print("4. Buscar item")
    print("5. Sair")

def adicionar_item(lista):
    try:
        num = int(input("Digite o número para adicionar a lista: "))
        lista.append(num)
        print(f"{num} foi adicionado a lista.")
    except ValueError:
        print("Por favor, digite um número válido.")

def remover_item(lista):
    try:
        num = int(input("Digite o número para remover da lista: "))
        if num in lista:
            lista.remove(num)
            print(f"{num} foi removido da lista.")
        else:
            print("Número não encontrado na lista.")
    except ValueError:
        print("Por favor, digite um número válido.")

def listar_item(lista):
    print("Lista completa:", lista)

def buscar_item(lista):
    try:
        num = int(input("Digite o número que deseja encontrar: "))
        if num in lista:
            print(f"{num} foi encontrado na lista.")
        else:
            print("Número não encontrado na lista.")
    except ValueError:
        print("Por favor, digite um número válido.")

def main():
    lista = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_item(lista)
        elif opcao == "2":
            remover_item(lista)
        elif opcao == "3":
            listar_item(lista)
        elif opcao == "4":
            buscar_item(lista)
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()