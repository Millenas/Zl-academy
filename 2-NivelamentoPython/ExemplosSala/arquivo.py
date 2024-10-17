#arquivos - x - cria um arquivo, w - substitui o texto de um arquivo, r - realiza a leitura de um arquivo, a - adiciona um texto

import os

if(os.path.isfile("arquivo.txt")):
    print("O arquivo existe")

    #arquivo = open("arquivo.txt", "a")
    #arquivo.write("DELL\n")
    #arquivo.close()

    #arquivo = open("arquivo.txt", "r")
    #texto = arquivo.read()
    #print(texto)
    
    arquivo = open("arquivo.txt", "w")
    arquivo.write("MILLENA")
    arquivo.close()

else:
    print("não existe")
    arquivo = open("arquivo.txt", "x")
    arquivo.close()