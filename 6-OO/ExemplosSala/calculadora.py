class Calculadora:
    def adicionar(self, a, b=0, c=0):
        return a + b + c
calc = Calculadora()
print(calc.adicionar(5))
print(calc.adicionar(5, 10))
print(calc.adicionar(5, 10, 15))