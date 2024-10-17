lista = ["carne", "frango", "arroz"]

while True:
    print("......................")
    print("1 - Exibir Lista\n2 - Adicionar item\n3 - Remover item\n4 - Verificar item")

    op = int(input("Digite a opção"))

    match(op):
        case 1:
            print(lista)
        case 2:
            item = input("Digite o novo item")
            lista.append(item)
            print("irem adicionado")
        case 3:
            item = input("Digite o item a ser emovido")
            if(item in lista):
                lista.remove(item)
                print(f"{item} removido da lista")
            else:
                print(f"{item} nao esta na lista")
        case 4:
            item = input("Digite o item a pesquisar")
            if(item in lista):
                print(f"{item} esta na lista")
            else:
                print(f"{item} nao esta na lista")