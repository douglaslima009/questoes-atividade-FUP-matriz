def carregar_matriz():
    matriz = []
    for _ in range(8):
        linha = []
        for _ in range(6):
            valor = int(input("Digite um valor para a matriz: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def calcular_media_linhas_pares(matriz):
    soma = 0
    contador = 0
    for i in range(1, len(matriz), 2):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            contador += 1
    media = soma / contador
    return media

matriz = carregar_matriz()

media_linhas_pares = calcular_media_linhas_pares(matriz)

print("A média dos elementos das linhas pares é:", media_linhas_pares)