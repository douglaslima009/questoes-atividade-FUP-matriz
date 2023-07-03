matriz = [[0] * 5 for _ in range(5)]

for i in range(5):
    matriz[i][i] = 1

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  