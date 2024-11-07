class SaldoInsuficienteError(Exception):
    def __init__(self, message="Saldo insuficiente para realizar o saque."):
        self.message = message
        super().__init__(self.message)

class LimiteExcedidoError(Exception):
    def __init__(self, message="Valor da transferência excede o limite da conta."):
        self.message = message
        super().__init__(self.message)

class ContaDestinoInvalidaError(Exception):
    def __init__(self, message="A conta destino não existe."):
        self.message = message
        super().__init__(self.message)

class Conta:
    def __init__(self, titular, saldo=0, limite=1000):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {self.saldo}")
        else:
            print("Valor de depósito deve ser positivo.")
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(f"Saldo disponível: {self.saldo}. Tentativa de saque: {valor}.")
        self.saldo -= valor
        print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
    
    def transferir(self, valor, conta_destino):
        if valor > self.limite:
            raise LimiteExcedidoError(f"Valor de transferência: {valor} ultrapassa o limite da conta.")
        if not isinstance(conta_destino, Conta):
            raise ContaDestinoInvalidaError("Conta de destino inválida.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar a transferência.")
        self.saldo -= valor
        conta_destino.depositar(valor)
        print(f"Transferência de {valor} para {conta_destino.titular} realizada com sucesso.")


if __name__ == "__main__":
    conta1 = Conta("João", 500)
    conta2 = Conta("Maria", 300, 1500)
    
    try:
        conta1.sacar(600)
    except SaldoInsuficienteError as e:
        print(f"Erro: {e}")

    try:
        conta1.transferir(600, "ContaInexistente")  # Passando um valor errado para a conta destino
    except ContaDestinoInvalidaError as e:
        print(f"Erro: {e}")

    try:
        conta1.transferir(1200, conta2)  # Transferindo mais do que o limite
    except LimiteExcedidoError as e:
        print(f"Erro: {e}")
    
    try:
        conta1.transferir(400, conta2)  # Transferência válida
    except Exception as e:
        print(f"Erro inesperado: {e}")
