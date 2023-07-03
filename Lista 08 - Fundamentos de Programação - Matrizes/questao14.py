def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            valor = float(input("Digite um número real: "))
            linha.append(valor)
        matriz.append(linha)
    
    return matriz

def somar_matrizes(matriz_a, matriz_b):
    matriz_c = []
    for i in range(len(matriz_a)):
        linha_c = []
        for j in range(len(matriz_a[i])):
            soma = matriz_a[i][j] + matriz_b[i][j]
            linha_c.append(soma)
        matriz_c.append(linha_c)
    
    return matriz_c

print("Preencha a matriz A:")
matriz_a = criar_matriz(17, 10)

print("Preencha a matriz B:")
matriz_b = criar_matriz(17, 10)

matriz_c = somar_matrizes(matriz_a, matriz_b)

print("Matriz C = A + B:")
for linha in matriz_c:
    print(linha)