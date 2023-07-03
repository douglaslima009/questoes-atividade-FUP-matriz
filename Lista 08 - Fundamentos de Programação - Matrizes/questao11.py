matriz = []
for i in range(22):
    linha = []
    for j in range(22):
        linha.append(int(input(f"Digite o valor para a posição [{i}][{j}]: ")))
    matriz.append(linha)

soma_diagonal_secundaria = 0
for i in range(22):
    soma_diagonal_secundaria += matriz[i][21-i]

print("Matriz:")
for linha in matriz:
    print(linha)
print("Soma da diagonal secundária:", soma_diagonal_secundaria)
