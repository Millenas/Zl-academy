#exemplo 2

import numpy as np

matriz = np.zeros((3,3), type(int))

for i in range(3):
    for j in range(3):
        matriz[i,j] = int(input(f"[{i+1}][{j+1}]: "))

soma = np.sum(matriz)
matrizT = np.transpose(matriz)
produto = np.dot(matriz,matrizT)

print(matriz)
print(soma)
print(matrizT)
print(produto)

