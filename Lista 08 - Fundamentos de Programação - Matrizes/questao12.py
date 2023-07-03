matriz = []
for i in range(56):
    linha = []
    for j in range(7):
        linha.append(int(input(f"Digite o valor para a posição [{i}][{j}]: ")))
    matriz.append(linha)

transposta = []
for j in range(7):
    coluna = []
    for i in range(56):
        coluna.append(matriz[i][j])
    transposta.append(coluna)

print("Matriz original:")
for linha in matriz:
    print(linha)

print("Transposta:")
for linha in transposta:
    print(linha)