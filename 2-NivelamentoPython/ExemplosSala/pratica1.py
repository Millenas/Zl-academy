#pratica1

#crie um programa capaz de criar uma matriz quadrada (n x n) e que calcule e exiba:
# -  a soma dos elementos da diagonal principal, - a soma dos elementos da diagonal secundária - a soma dos elementos da diagonal principal com a secundaria
import numpy as np

somaDp =0
somaDs=0

n = int(input("Digite o tamanho da matriz (n x n): "))
matriz = np.zeros((n,n), type(int))

for i in range(n):
    for j in range(n):
        matriz[i,j] = int(input(f"[{i+1}][{j+1}]: "))

        if(i==j):
            somaDp+=matriz[i][j]
        if(i == n-i-1):
            somaDs+=matriz[i][j]

print(matriz)
print(somaDp)
print(somaDs)
print(somaDp+somaDs)




