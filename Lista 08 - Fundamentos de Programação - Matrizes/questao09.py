import random

def preencher_matriz():
    matriz = []
    for _ in range(18):
        linha = []
        for _ in range(18):
            linha.append(random.randint(1, 100))
        matriz.append(linha)
    return matriz

def calcular_soma_abaixo_diagonal(matriz):
    soma = 0
    for i in range(18):
        for j in range(i):
            soma += matriz[i][j]
    return soma

matriz = preencher_matriz()
soma_abaixo_diagonal = calcular_soma_abaixo_diagonal(matriz)

for linha in matriz:
    print(linha)

print("Soma abaixo da diagonal principal:", soma_abaixo_diagonal)