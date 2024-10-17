class Imc:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calculo_imc(self):
        return self.peso / (self.altura * self.altura)

    def faixa_peso(self):
        imc = self.calculo_imc()
        if imc < 18.5:
            return "Magreza"
        elif 18.5 <= imc < 24.9:
            return "Normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 39.9:
            return "Obesidade"
        else:
            return "Obesidade Grave"

    
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

pessoa = Imc(peso, altura)

imc = pessoa.calculo_imc()
print(f"\nSeu IMC é: {imc:.2f}")
print(f"Faixa de peso: {pessoa.faixa_peso()}")
