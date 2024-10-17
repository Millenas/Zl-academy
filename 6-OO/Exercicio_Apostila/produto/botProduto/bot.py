import json
from botcity.web import WebBot, Browser, By
from botcity.maestro import *

# Classe Produto
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    # Getters e Setters
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            print("Nome deve ser uma string.")

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Preço deve ser um número maior ou igual a 0.")

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            print("Quantidade deve ser um número inteiro maior ou igual a 0.")

def salvar_dados_em_json(produtos):
    dados = [{"nome": produto.nome, "preco": produto.preco, "quantidade": produto.quantidade} for produto in produtos]

    # Escreve os dados no arquivo JSON
    with open("dados.json", "w", encoding="utf-8") as arquivo_json:
        json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)

    print("Dados salvos no arquivo dados.json")

def main():
    # Cria uma lista de objetos Produto
    produtos = [
        Produto("TV", 500, 20),
        Produto("Camiseta", 50, 150),
        Produto("Computador", 2000, 10),
        Produto("Notebook", 2500, 30)
    ]

    # Inicializa o bot
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.EDGE
    bot.driver_path = r"C:\Users\matutino\Desktop\ZlAcademy-Millena\POO\produto\botProduto\resources\msedgedriver.exe"

    bot.browse("http://127.0.0.1:5500/forms.html")

    for produto in produtos:
        bot.find_element("nome", By.ID).send_keys(produto.nome)
        bot.wait(1000)
        bot.find_element("preco", By.ID).send_keys(str(produto.preco))  
        bot.wait(1000)
        bot.find_element("quantidade", By.ID).send_keys(str(produto.quantidade))  
        bot.wait(1000)

        bot.find_element("forms", By.ID).click()
        bot.wait(1000)  

        bot.find_element("nome", By.ID).clear()
        bot.find_element("preco", By.ID).clear()
        bot.find_element("quantidade", By.ID).clear()

    # Salvar os dados dos produtos em um arquivo JSON
    salvar_dados_em_json(produtos)


    bot.wait(3000)

    bot.stop_browser()

def not_found(label):
    print(f"Elemento não encontrado: {label}")

if __name__ == '__main__':
    main()
