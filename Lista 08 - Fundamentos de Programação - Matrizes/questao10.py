import random

def preencher_matriz():
    matriz = []
    for _ in range(22):
        linha = []
        for _ in range(22):
            linha.append(random.randint(1, 100))
        matriz.append(linha)
    return matriz

def calcular_soma_diagonal_principal(matriz):
    soma = 0
    for i in range(22):
        soma += matriz[i][i]
    return soma

matriz = preencher_matriz()
soma_diagonal_principal = calcular_soma_diagonal_principal(matriz)

for linha in matriz:
    print(linha)

print("Soma da diagonal principal:", soma_diagonal_principal)