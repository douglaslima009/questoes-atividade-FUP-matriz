matriz = [[0] * 13 for _ in range(12)]

for i in range(12):
    for j in range(13):
        matriz[i][j] = i * j

print("Matriz original:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()

for linha in matriz:
    max_elemento = max(linha, key=abs)
    for i in range(13):
        linha[i] -= max_elemento

print("\nMatriz modificada:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()