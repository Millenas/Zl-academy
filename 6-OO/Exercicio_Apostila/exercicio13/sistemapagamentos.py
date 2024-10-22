import tkinter as tk
from tkinter import messagebox

class Funcionario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        super().__init__(nome, matricula)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self.salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.salario_mensal

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self.salario_base = salario_base
        self.vendas = vendas
        self.taxa_comissao = taxa_comissao

    def calcular_salario(self):
        return self.salario_base + (self.vendas * self.taxa_comissao)

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Funcionários")
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Nome:").grid(row=0)
        self.nome_entry = tk.Entry(self.master)
        self.nome_entry.grid(row=0, column=1)
        

        tk.Label(self.master, text="Matrícula:").grid(row=1)
        self.matricula_entry = tk.Entry(self.master)
        self.matricula_entry.grid(row=1, column=1)
        
        tk.Label(self.master, text="Tipo:").grid(row=2)
        self.tipo_var = tk.StringVar(value="horista")
        tk.Radiobutton(self.master, text="Horista", variable=self.tipo_var, value="horista").grid(row=2, column=1)
        tk.Radiobutton(self.master, text="Mensalista", variable=self.tipo_var, value="mensalista").grid(row=3, column=1)
        tk.Radiobutton(self.master, text="Comissionado", variable=self.tipo_var, value="comissionado").grid(row=4, column=1)

        tk.Label(self.master, text="Horas Trabalhadas:").grid(row=5)
        self.horas_entry = tk.Entry(self.master)
        self.horas_entry.grid(row=5, column=1)

        tk.Label(self.master, text="Valor Hora:").grid(row=6)
        self.valor_hora_entry = tk.Entry(self.master)
        self.valor_hora_entry.grid(row=6, column=1)

        tk.Label(self.master, text="Salário Mensal:").grid(row=7)
        self.salario_entry = tk.Entry(self.master)
        self.salario_entry.grid(row=7, column=1)

        tk.Label(self.master, text="Vendas:").grid(row=8)
        self.vendas_entry = tk.Entry(self.master)
        self.vendas_entry.grid(row=8, column=1)

        tk.Label(self.master, text="Taxa Comissão:").grid(row=9)
        self.taxa_entry = tk.Entry(self.master)
        self.taxa_entry.grid(row=9, column=1)

        self.cadastrar_button = tk.Button(self.master, text="Cadastrar", command=self.cadastrar_funcionario)
        self.cadastrar_button.grid(row=10, column=0)

        self.sair_button = tk.Button(self.master, text="Sair", command=self.master.quit)
        self.sair_button.grid(row=10, column=1)

    def cadastrar_funcionario(self):
        nome = self.nome_entry.get()
        matricula = self.matricula_entry.get()
        tipo = self.tipo_var.get()

        if tipo == "horista":
            horas = float(self.horas_entry.get())
            valor_hora = float(self.valor_hora_entry.get())
            funcionario = FuncionarioHorista(nome, matricula, horas, valor_hora)
        elif tipo == "mensalista":
            salario_mensal = float(self.salario_entry.get())
            funcionario = FuncionarioMensalista(nome, matricula, salario_mensal)
        elif tipo == "comissionado":
            salario_base = float(self.salario_entry.get())
            vendas = float(self.vendas_entry.get())
            taxa_comissao = float(self.taxa_entry.get())
            funcionario = FuncionarioComissionado(nome, matricula, salario_base, vendas, taxa_comissao)

        messagebox.showinfo("Cadastro", f"Funcionário {funcionario.nome} cadastrado com sucesso!\nSalário: {funcionario.calcular_salario():.2f}")

        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
