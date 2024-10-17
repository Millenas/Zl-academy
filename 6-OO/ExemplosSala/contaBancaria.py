class ContaBancaria:
    taxa_juros = 0.02

    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    # Métodos de instância para depositar dinheiro
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do déposito deve ser positivo.")

    # Método de instâncias para sacar dinheiro
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print(f"Saldo insuficiente ou valor de saque inválido.")

    # Método de instância para exibir o saldo
    def mostrar_saldo(self):
        print(f"Saldo de {self.titular}: R${self.__saldo:.2f}")
    

    # Método de classe como construtor alternativo
    @classmethod
    def conta_com_juros(cls, titular, saldo_inicial):
        saldo_com_juros = saldo_inicial * (1 + cls.taxa_juros)
        return cls(titular, saldo_com_juros)

# Criando objetos da classe ContaBancaria usando o contrutor padrão 
conta1 = ContaBancaria("Millena", 5800)
# # Criando objetos da classe ContaBancaria usando o construtor de classe
conta2 = ContaBancaria.conta_com_juros("Bob", 1000)

# Usando Método Name mangling
conta1.mostrar_saldo()
conta1.depositar(150)
conta1.sacar(100)
conta1.mostrar_saldo()

conta2.mostrar_saldo()
conta2.depositar(650)
conta2.sacar(300)
conta2.mostrar_saldo()

