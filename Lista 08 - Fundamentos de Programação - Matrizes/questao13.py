def gerar_vetor_soma_colunas(matriz):
    vetor_soma = []
    num_colunas = len(matriz[0])

    for coluna in range(num_colunas):
        soma = 0
        for linha in matriz:
            soma += linha[coluna]
        vetor_soma.append(soma)

    return vetor_soma

def criar_matriz():
    matriz = []
    print("Digite os valores da matriz:")
    for _ in range(17):
        linha = []
        for _ in range(17):
            valor = float(input("Digite um número real: "))
            linha.append(valor)
        matriz.append(linha)
    
    return matriz

matriz = criar_matriz()
vetor_soma = gerar_vetor_soma_colunas(matriz)

print("Vetor de soma das colunas:")
print(vetor_soma)