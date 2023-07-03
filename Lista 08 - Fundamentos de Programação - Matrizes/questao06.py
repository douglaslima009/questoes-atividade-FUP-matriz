def preencher_matriz():
    matriz = []
    for _ in range(11):
        linha = []
        for _ in range(15):
            valor = int(input("Digite um valor para a matriz: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def criar_terceira_matriz(matriz1, matriz2):
    matriz3 = []
    for i in range(11):
        linha = []
        for j in range(15):
            valor1 = matriz1[i][j]
            valor2 = matriz2[i][j]
            maior_valor = max(valor1, valor2)
            linha.append(maior_valor)
        matriz3.append(linha)
    return matriz3

print("Preencha a primeira matriz 11x15:")
matriz1 = preencher_matriz()

print("Preencha a segunda matriz 11x15:")
matriz2 = preencher_matriz()

matriz3 = criar_terceira_matriz(matriz1, matriz2)

print("Terceira matriz com os maiores valores:")
for linha in matriz3:
    print(linha)