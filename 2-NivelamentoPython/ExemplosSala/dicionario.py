#pratica1

#Vc é um pesquisador de novas espécies de animais e precisa adicionar um novo dado em um dicionário existente. 
# Crie um programa capaz de adicionar um dado a um dicionário e exibi-lo sempre que o usuário desejar.
dicionario_especies = {}

while True:
    print("....******BEM-VINDO (A) DICIONÁRIO DE ANIMAIS********.....")
    print("1 - Adicionar nova espécie\n2 - Exibir todas as espécies\n3 - Sair")

    op = int(input("Digite a opção: "))

    match(op):
        case 1:
            nome = input("Digite o nome da espécie: ")
            habitat = input("Digite o habitat da espécie: ")
            descricao = input("Digite a descrição da espécie: ")
    
            dicionario_especies[nome] = {
            "Habitat": habitat,
            "Descrição": descricao
             }
            print("Espécie adicionado")
        case 2:
            if not dicionario_especies:
                print("Nenhuma espécie encontrada.")
    
            for nome, details in dicionario_especies.items():
                print(f"Nome da Espécie: {nome}")
                print(f"Habitat: {details['Habitat']}")
                print(f"Descrição: {details['Descrição']}")
                print("----------------------------")

        case 3:
            print("Saindo do programa.")
            break
        case _:
                print("Opção inválida, por favor tente novamente.")







