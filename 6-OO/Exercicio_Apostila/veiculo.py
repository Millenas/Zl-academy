class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info_veiculo(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        Veiculo.__init__(self, marca, modelo)
        self.numero_portas = numero_portas
    
    def informacao_completa(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Número de portas: {self.numero_portas}")


carro = Carro("Toyota", "Corolla", 4)
carro.informacao_completa()
