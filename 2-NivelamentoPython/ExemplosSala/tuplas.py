#tupla = (0,1,2,3,4,5)

#print(tupla[0])
#print(tupla[-1])
#print(tupla[:3])  

#exemplo 2

#Crie um programa que armazene n registros de estudantes como nome, idade e nota. em seguida exiba os registros
n = int(input("Digite o numero de registros de estudantes: "))

Registros_estudantes =  []

for i in range(n):
    tupla = input("Digite o nome, idade e nota do estudante: ").split()
    nome = tupla[0]
    idade = int(tupla [1])
    nota = int(tupla [2])

    Registros_estudantes.append((nome,idade,nota))

print(Registros_estudantes)