from functools import reduce

# Classe Venda
class Venda:
    def __init__(self, nome_produto, quantidade, preco_unitario):
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def total(self):
        return self.quantidade * self.preco_unitario

# Classe HistoricoVendas
class HistoricoVendas:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    def total_por_produto(self):
        totals = reduce(
            lambda acc, venda: {**acc, venda.nome_produto: acc.get(venda.nome_produto, 0) + venda.total()},
            self.vendas,
            {}
        )
        return totals

    def listar_vendas_acima_de(self, valor):
        for venda in self.vendas:
            if venda.total() > valor:
                yield venda

# Decorador para autenticar acesso
def autenticar_acesso(func):
    def wrapper(self, funcionario, *args, **kwargs):
        if funcionario.cargo != "Gerente":
            print("Acesso negado. Apenas gerentes podem aumentar salários.")
            return
        return func(self, funcionario, *args, **kwargs)
    return wrapper

# Classe Funcionario
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

# Classe SistemaRH
class SistemaRH:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    @autenticar_acesso
    def aumentar_salario(self, funcionario, percentual):
        funcionario.salario += funcionario.salario * percentual / 100
        print(f"Salário de {funcionario.nome} aumentado para {funcionario.salario}")

# Classe Conta
class Conta:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor):
        self.transacoes.append((tipo, valor))

    def filtrar_transacoes_por_tipo(self, tipo):
        return list(filter(lambda t: t[0] == tipo, self.transacoes))

    def aplicar_taxa(self, taxa):
        self.transacoes = list(map(lambda t: (t[0], t[1] * (1 - taxa)) if t[0] == "Saque" else t, self.transacoes))

# Exemplo de uso
if __name__ == "__main__":

    historico = HistoricoVendas()
    historico.adicionar_venda(Venda("Notebook", 1, 3500))
    historico.adicionar_venda(Venda("Monitor", 1, 290))
    historico.adicionar_venda(Venda("Teclado", 1, 90))

    print("Total por produto:", historico.total_por_produto())
    for venda in historico.listar_vendas_acima_de(300):
        print(f"Venda acima de 300: {venda.nome_produto} - Total: {venda.total()}")

    sistema_rh = SistemaRH()
    funcionario1 = Funcionario("Millena", "Gerente", 3500)
    funcionario2 = Funcionario("Maria", "Analista", 2500)

    sistema_rh.adicionar_funcionario(funcionario1)
    sistema_rh.adicionar_funcionario(funcionario2)

    sistema_rh.aumentar_salario(funcionario1, 10)  
    sistema_rh.aumentar_salario(funcionario2, 10)  

    conta = Conta()
    conta.adicionar_transacao("Depósito", 200)
    conta.adicionar_transacao("Saque", 50)
    conta.adicionar_transacao("Saque", 20)

    print("Transações de Saque:", conta.filtrar_transacoes_por_tipo("Saque"))
    conta.aplicar_taxa(0.1) #taxa de 10%
    print("Transações após aplicar taxa:", conta.transacoes)
