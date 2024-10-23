<<<<<<< HEAD
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @property
    def matricula(self):
        return self._matricula

    @abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        super().__init__(nome, matricula)
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_hora = valor_hora

    @property
    def horas_trabalhadas(self):
        return self._horas_trabalhadas

    @horas_trabalhadas.setter
    def horas_trabalhadas(self, value):
        if value < 0:
            raise ValueError("Horas trabalhadas não podem ser negativas.")
        self._horas_trabalhadas = value

    @property
    def valor_hora(self):
        return self._valor_hora

    @valor_hora.setter
    def valor_hora(self, value):
        if value < 0:
            raise ValueError("Valor por hora não pode ser negativo.")
        self._valor_hora = value

    def calcular_salario(self):
        return self._horas_trabalhadas * self._valor_hora

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self._salario_mensal = salario_mensal

    @property
    def salario_mensal(self):
        return self._salario_mensal

    def calcular_salario(self):
        return self._salario_mensal

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self._salario_base = salario_base
        self._vendas = vendas
        self._taxa_comissao = taxa_comissao

    @property
    def salario_base(self):
        return self._salario_base

    @property
    def vendas(self):
        return self._vendas

    @property
    def taxa_comissao(self):
        return self._taxa_comissao

    def calcular_salario(self):
        return self._salario_base + (self._vendas * self._taxa_comissao)


def processar_pagamento(funcionario):
    print(f"Funcionário: {funcionario.nome}, Salário: {funcionario.calcular_salario():.2f}")


def simular_pagamentos(funcionarios):
    for funcionario in funcionarios:
        processar_pagamento(funcionario)


if __name__ == "__main__":

    funcionarios = [
        FuncionarioHorista("Alice", "H001", 160, 25.0),  # 160 horas, R$25/hora
        FuncionarioMensalista("Bob", "M001", 3000.0),   # Salário mensal R$3000
        FuncionarioComissionado("Charlie", "C001", 2000.0, 10000.0, 0.10)  # R$2000 + 10% de R$10000
    ]

    simular_pagamentos(funcionarios)
=======
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @property
    def matricula(self):
        return self._matricula

    @abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        super().__init__(nome, matricula)
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_hora = valor_hora

    @property
    def horas_trabalhadas(self):
        return self._horas_trabalhadas

    @horas_trabalhadas.setter
    def horas_trabalhadas(self, value):
        if value < 0:
            raise ValueError("Horas trabalhadas não podem ser negativas.")
        self._horas_trabalhadas = value

    @property
    def valor_hora(self):
        return self._valor_hora

    @valor_hora.setter
    def valor_hora(self, value):
        if value < 0:
            raise ValueError("Valor por hora não pode ser negativo.")
        self._valor_hora = value

    def calcular_salario(self):
        return self._horas_trabalhadas * self._valor_hora

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self._salario_mensal = salario_mensal

    @property
    def salario_mensal(self):
        return self._salario_mensal

    def calcular_salario(self):
        return self._salario_mensal

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self._salario_base = salario_base
        self._vendas = vendas
        self._taxa_comissao = taxa_comissao

    @property
    def salario_base(self):
        return self._salario_base

    @property
    def vendas(self):
        return self._vendas

    @property
    def taxa_comissao(self):
        return self._taxa_comissao

    def calcular_salario(self):
        return self._salario_base + (self._vendas * self._taxa_comissao)


def processar_pagamento(funcionario):
    print(f"Funcionário: {funcionario.nome}, Salário: {funcionario.calcular_salario():.2f}")


def simular_pagamentos(funcionarios):
    for funcionario in funcionarios:
        processar_pagamento(funcionario)


if __name__ == "__main__":

    funcionarios = [
        FuncionarioHorista("Alice", "H001", 160, 25.0),  # 160 horas, R$25/hora
        FuncionarioMensalista("Bob", "M001", 3000.0),   # Salário mensal R$3000
        FuncionarioComissionado("Charlie", "C001", 2000.0, 10000.0, 0.10)  # R$2000 + 10% de R$10000
    ]

    simular_pagamentos(funcionarios)
>>>>>>> 27445d1a72059d8e00f7581a3e3c70500722a980
