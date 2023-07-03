matriz = [[0] * 4 for _ in range(4)] 

for i in range(4):
    for j in range(4):
        matriz[i][j] = (i + 1) * (j + 1)

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  