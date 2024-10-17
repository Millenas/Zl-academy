class Pessoa:
    def __init__(self, nome='', idade=0, peso=0.0, altura=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5 

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros

    def __str__(self):
        return (f'Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} kg, '
                f'Altura: {self.altura} cm')

if __name__ == "__main__":

    pessoa = Pessoa(nome="Millena", idade=26, peso=80.0, altura=156.0)

    print(pessoa)

    pessoa.envelhecer()
    print("Após envelhecer:")
    print(pessoa)

    pessoa.engordar(2)
    print("Após engordar 2 kg:")
    print(pessoa)

    pessoa.emagrecer(1)
    print("Após emagrecer 1 kg:")
    print(pessoa)

    pessoa.crescer(2)  
    print("Após crescer 2 cm:")
    print(pessoa)
