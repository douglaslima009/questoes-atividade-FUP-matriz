import random

def gerar_matriz():
    matriz = []
    for _ in range(10):
        linha = []
        for _ in range(10):
            valor = random.randint(-103, 705)
            linha.append(valor)
        matriz.append(linha)
    return matriz

def transformar_em_triangulo_inferior(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            matriz[i][j] = 0
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

matriz_original = gerar_matriz()

print("Matriz original:")
imprimir_matriz(matriz_original)

matriz_transformada = transformar_em_triangulo_inferior(matriz_original)

print("Matriz transformada:")
imprimir_matriz(matriz_transformada)