import json
import csv
import pickle
from functools import reduce

# Classe Livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

    def __repr__(self):
        return f"'{self.titulo}' de {self.autor} ({self.ano_publicacao}) - {self.genero}"

# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros_por_autor(self, autor):
        return list(filter(lambda livro: livro.autor == autor, self.livros))

    def contar_livros_por_genero(self, genero):
        return reduce(lambda count, livro: count + 1 if livro.genero == genero else count, self.livros, 0)

    def exportar_texto(self, filename="biblioteca.txt"):
        with open(filename, 'w', encoding='utf-8') as file:
            for livro in self.livros:
                file.write(f"{livro.titulo} - {livro.autor} - {livro.ano_publicacao} - {livro.genero}\n")

    def exportar_json(self, filename="biblioteca.json"):
        livros_dict = [vars(livro) for livro in self.livros]
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(livros_dict, file, ensure_ascii=False, indent=4)

    def exportar_csv(self, filename="biblioteca.csv"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Título", "Autor", "Ano de Publicação", "Gênero"])
            for livro in self.livros:
                writer.writerow([livro.titulo, livro.autor, livro.ano_publicacao, livro.genero])

    def exportar_binario(self, filename="biblioteca.pkl"):
        with open(filename, 'wb') as file:
            pickle.dump(self.livros, file)

    def importar_texto(self, filename="biblioteca.txt"):
        with open(filename, 'r', encoding='utf-8') as file:
            for linha in file:
                titulo, autor, ano_publicacao, genero = linha.strip().split(" - ")
                livro = Livro(titulo, autor, int(ano_publicacao), genero)
                self.adicionar_livro(livro)

    def importar_json(self, filename="biblioteca.json"):
        with open(filename, 'r', encoding='utf-8') as file:
            livros_dict = json.load(file)
            for livro_dict in livros_dict:
                livro = Livro(**livro_dict)
                self.adicionar_livro(livro)

    def importar_csv(self, filename="biblioteca.csv"):
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Ignorar cabeçalho
            for row in reader:
                titulo, autor, ano_publicacao, genero = row
                livro = Livro(titulo, autor, int(ano_publicacao), genero)
                self.adicionar_livro(livro)

    def importar_binario(self, filename="biblioteca.pkl"):
        with open(filename, 'rb') as file:
            self.livros = pickle.load(file)

    def filtrar_livros(self, ano=None, genero=None):
        return list(filter(lambda livro: (ano is None or livro.ano_publicacao == ano) and (genero is None or livro.genero == genero), self.livros))

    def backup(self, formato="binario"):
        if formato == "binario":
            self.exportar_binario("backup.pkl")
        elif formato == "json":
            self.exportar_json("backup.json")
        else:
            print("Formato de backup inválido.")

def gerar_relatorio_titulos(biblioteca):
    return list(map(lambda livro: livro.titulo, biblioteca.livros))

def gerar_relatorio_livros_por_genero(biblioteca, genero):
    return biblioteca.contar_livros_por_genero(genero)

if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Adicionando livros à biblioteca
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia")
    livro2 = Livro("1984", "George Orwell", 1949, "Distopia")
    livro3 = Livro("Fundação", "Isaac Asimov", 1951, "Ficção científica")
    livro4 = Livro("A Guerra dos Tronos", "George R.R. Martin", 1996, "Fantasia")
    livro5 = Livro("Dom Casmurro", "Machado de Assis", 1899, "Literatura Brasileira")
    livro6 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 1997, "Romance")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)
    biblioteca.adicionar_livro(livro4)
    biblioteca.adicionar_livro(livro5)
    biblioteca.adicionar_livro(livro6)

    # Teste de funcionalidade
    print("Livros de George Orwell:", biblioteca.listar_livros_por_autor("George Orwell"))
    print("Número de livros de Fantasia:", biblioteca.contar_livros_por_genero("Fantasia"))
    
    # Exportar dados
    biblioteca.exportar_texto()
    biblioteca.exportar_json()
    biblioteca.exportar_csv()
    biblioteca.exportar_binario()

    # Backup de dados
    biblioteca.backup(formato="json")

    # Filtrar livros
    livros_filtrados = biblioteca.filtrar_livros(ano=1954, genero="Fantasia")
    print("Livros filtrados (1954, Fantasia):", livros_filtrados)

    # Gerar relatórios
    titulos = gerar_relatorio_titulos(biblioteca)
    print("Títulos de todos os livros:", titulos)
    
    num_livros_fantasia = gerar_relatorio_livros_por_genero(biblioteca, "Fantasia")
    print("Número de livros de Fantasia:", num_livros_fantasia)
