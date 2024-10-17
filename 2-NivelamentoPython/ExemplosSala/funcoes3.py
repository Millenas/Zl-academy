#exemplo3 função com return

def potencia(a):
    quadrado = pow(a,2)
    return quadrado

numero = int(input("Digite um núemro: "))
resultado = potencia(numero)
print(f"O quadrado do número {numero} é {resultado}")
