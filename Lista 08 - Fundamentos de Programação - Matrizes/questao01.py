matriz = [[0] * 4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input(f"Digite o valor para a posição ({i + 1},{j + 1}): "))

maiorque10 = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            maiorque10 += 1

print(f"A matriz possui {maiorque10} valores maiores que 10.")