class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True


    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' já está emprestado.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já está disponível.")

    def mostrar_info(self):
        status = "disponível" if self.disponivel else "emprestado"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Status: {status}")


class Livraria:
    def __init__(self):
        self.livros = []  # Lista de livros na livraria

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"O livro '{livro.titulo}' foi adicionado ao inventário.")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f"O livro '{titulo}' não foi encontrado no inventário.")

    def mostrar_inventario(self):
        if self.livros:
            print("Inventário da Livraria:")
            for livro in self.livros:
                livro.mostrar_info()
        else:
            print("O inventário está vazio.")


# Exemplo de uso
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Morro dos Ventos Uivantes", "Emily Brontë")

livraria = Livraria()
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)

livraria.mostrar_inventario()

livraria.emprestar_livro("Dom Casmurro")
livraria.mostrar_inventario()

livraria.emprestar_livro("Dom Casmurro")  # Tentar emprestar novamente

livro1.devolver()
livraria.mostrar_inventario()