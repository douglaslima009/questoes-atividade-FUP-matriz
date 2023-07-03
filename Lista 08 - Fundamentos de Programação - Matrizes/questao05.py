def preencher_matriz():
    matriz = []
    for _ in range(13):
        linha = []
        for _ in range(10):
            valor = int(input("Digite um valor para a matriz: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return None

print("Preencha a matriz 13x10:")
matriz = preencher_matriz()

valor_x = int(input("Digite o valor que deseja buscar na matriz: "))

resultado = buscar_valor(matriz, valor_x)

if resultado:
    linha, coluna = resultado
    print(f"Valor encontrado na linha {linha+1}, coluna {coluna+1}.")
else:
    print("Valor não encontrado na matriz.")