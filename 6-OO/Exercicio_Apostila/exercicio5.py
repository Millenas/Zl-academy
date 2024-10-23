class Veiculo:
    total_veiculos = 0

    def __init__(self, nome, ano, valor_diario):
        self.__nome = nome
        self.__ano = ano
        self.__valor_diario = valor_diario
        Veiculo.total_veiculos += 1

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_valor_diario(self):
        return self.__valor_diario

    def set_valor_diario(self, valor):
        self.__valor_diario = valor

    @classmethod
    def get_total_veiculos(cls):
        return cls.total_veiculos

    @classmethod
    def aumentar_preco_diario(cls, percentual):
        for veiculo in cls.get_all_vehicles():
            veiculo.set_valor_diario(veiculo.get_valor_diario() * (1 + percentual / 100))

    def calcular_aluguel(self, dias, desconto=0, cupom=None):
        total = self.__valor_diario * dias
        total -= desconto

        if dias > 7:
            total *= 0.9 

        if cupom == "DESCONTO10":
            total *= 0.9 

        return total

class Carro(Veiculo):
    def __init__(self, nome, ano, valor_diario, tipo_combustivel):
        super().__init__(nome, ano, valor_diario)
        self.__tipo_combustivel = tipo_combustivel

    def calcular_aluguel(self, dias, desconto=0, cupom=None):
        total = super().calcular_aluguel(dias, desconto, cupom)
        return total

class Motocicleta(Veiculo):
    def __init__(self, nome, ano, valor_diario, cilindrada):
        super().__init__(nome, ano, valor_diario)
        self.__cilindrada = cilindrada

    def calcular_aluguel(self, dias, desconto=0, cupom=None):
        total = super().calcular_aluguel(dias, desconto, cupom)

        if self.__cilindrada > 200:
            total += 50  

        return total


carro1 = Carro("Fusca", 1972, 100, "Gasolina")
moto1 = Motocicleta("Honda CG", 2020, 50, 250)

print(carro1.calcular_aluguel(10))  
print(moto1.calcular_aluguel(10))   

print(Veiculo.get_total_veiculos()) 
