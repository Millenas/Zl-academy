from Autor import Autor  
from Livro import Livro  
from Biblioteca import Biblioteca
 
# Criando autores
autor1 = Autor("Machado de Assis")
autor2 = Autor("Clarice Lispector")

# Criando livros
livro1 = Livro("Dom Casmurro", autor1, "001")
livro2 = Livro("A Hora da Estrela", autor2, "002")

# Criando a biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Mostrando livros disponíveis
biblioteca.mostrar_livros_disponiveis()

# Registrando um empréstimo
biblioteca.registrar_emprestimo("001", "Carlos Souza")

# Mostrando livros disponíveis após empréstimo
biblioteca.mostrar_livros_disponiveis()

# Registrando devolução
biblioteca.registrar_devolucao("001")

# Mostrando livros disponíveis após devolução
biblioteca.mostrar_livros_disponiveis()

# Mostrando o total de livros
Biblioteca.mostrar_total_livros()
