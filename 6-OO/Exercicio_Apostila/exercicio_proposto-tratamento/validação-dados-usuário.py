class NomeVazioError(ValueError):
    def __init__(self, message="O nome não pode ser vazio."):
        self.message = message
        super().__init__(self.message)

class IdadeInvalidaError(TypeError):
    def __init__(self, message="Idade deve ser um número inteiro."):
        self.message = message
        super().__init__(self.message)

class EmailInvalidoError(ValueError):
    def __init__(self, message="Email deve conter um '@'."):
        self.message = message
        super().__init__(self.message)

class Usuario:
    def __init__(self, nome, idade, email):
        if not nome:
            raise NomeVazioError()
        if not isinstance(idade, int):
            raise IdadeInvalidaError()
        if "@" not in email:
            raise EmailInvalidoError()
        
        self.nome = nome
        self.idade = idade
        self.email = email


if __name__ == "__main__":
    try:
        usuario1 = Usuario("", 25, "joao@example.com")  # Nome vazio
    except NomeVazioError as e:
        print(f"Erro: {e}")

    try:
        usuario2 = Usuario("João", "vinte e cinco", "joao@example.com")  # Idade inválida
    except IdadeInvalidaError as e:
        print(f"Erro: {e}")

    try:
        usuario3 = Usuario("Maria", 30, "mariaexample.com")  # Email inválido
    except EmailInvalidoError as e:
        print(f"Erro: {e}")

    try:
        usuario4 = Usuario("Ana", 28, "ana@example.com")  # Dados válidos
        print(f"Usuário {usuario4.nome} criado com sucesso.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
