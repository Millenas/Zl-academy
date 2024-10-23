import tkinter as tk
from tkinter import messagebox

class VeiculoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento de Veículos")

        self.nome_label = tk.Label(root, text="Nome do Veículo:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(root)
        self.nome_entry.pack()

        self.ano_label = tk.Label(root, text="Ano do Veículo:")
        self.ano_label.pack()
        self.ano_entry = tk.Entry(root)
        self.ano_entry.pack()

        self.valor_label = tk.Label(root, text="Valor Diário:")
        self.valor_label.pack()
        self.valor_entry = tk.Entry(root)
        self.valor_entry.pack()

        self.tipo_label = tk.Label(root, text="Tipo de Combustível:")
        self.tipo_label.pack()
        self.tipo_combobox = tk.StringVar()
        self.tipo_combobox.set("Gasolina") 
        tk.OptionMenu(root, self.tipo_combobox, "Gasolina", "Etanol", "Diesel").pack()

        self.cilindrada_label = tk.Label(root, text="Cilindrada:")
        self.cilindrada_label.pack()
        self.cilindrada_entry = tk.Entry(root)
        self.cilindrada_entry.pack()

        self.dias_label = tk.Label(root, text="Número de Dias:")
        self.dias_label.pack()
        self.dias_entry = tk.Entry(root)
        self.dias_entry.pack()

        self.add_button = tk.Button(root, text="Adicionar Veículo", command=self.adicionar_veiculo)
        self.add_button.pack()

        self.calcular_button = tk.Button(root, text="Calcular Aluguel", command=self.calcular_aluguel)
        self.calcular_button.pack()

        self.sair_button = tk.Button(root, text="Sair", command=root.destroy)
        self.sair_button.pack()
        
    def adicionar_veiculo(self):
        nome = self.nome_entry.get()
        ano = self.ano_entry.get()
        valor = self.valor_entry.get()
        tipo_combustivel = self.tipo_combobox.get()
        cilindrada = self.cilindrada_entry.get()

        print(f"Veículo Adicionado: {nome}, {ano}, {valor}, {tipo_combustivel}, {cilindrada}")
        messagebox.showinfo("Sucesso", "Veículo adicionado com sucesso!")

    def calcular_aluguel(self):
        try:
            valor_diario = float(self.valor_entry.get())
            dias = int(self.dias_entry.get())
            tipo_combustivel = self.tipo_combobox.get()
            cilindrada = int(self.cilindrada_entry.get())

            total = valor_diario * dias

            if dias > 7:
                total *= 0.9  

            if cilindrada > 200:
                total += 50  

            messagebox.showinfo("Custo do Aluguel", f"O custo total do aluguel é: R$ {total:.2f}")

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VeiculoApp(root)
    root.mainloop()