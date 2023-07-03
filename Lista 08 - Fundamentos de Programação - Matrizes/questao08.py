import random

def preencher_matriz():
    matriz = []
    for _ in range(20):
        linha = []
        for _ in range(20):
            linha.append(random.randint(1, 100)) 
        matriz.append(linha)
    return matriz

def calcular_soma_acima_diagonal(matriz):
    soma = 0
    for i in range(20):
        for j in range(i+1, 20):
            soma += matriz[i][j]
    return soma

matriz = preencher_matriz()
soma_acima_diagonal = calcular_soma_acima_diagonal(matriz)

for linha in matriz:
    print(linha)

print("Soma acima da diagonal principal:", soma_acima_diagonal)