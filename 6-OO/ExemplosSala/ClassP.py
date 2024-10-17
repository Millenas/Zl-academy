class Pessoa:
    n_pessoas = 0

    def __init__(self, nome, idade):
        self.nomme = nome
        self.idade = idade
        Pessoa.n_pessoas += 1

    @classmethod
    def total_pessoas (cls):
        print(f"total de pessoas: {cls.n_pessoas}")

pessoa1 = Pessoa("Millena", 26)
pessoa2 = Pessoa("Mirela", 9)

Pessoa.total_pessoas()