import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

matriz = [[0] * 13 for _ in range(12)]

for i in range(12):
    for j in range(13):
        matriz[i][j] = i + j

print("Matriz original:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()

for j in range(13):
    coluna = [matriz[i][j] for i in range(12)]
    max_primo = None
    for elemento in coluna:
        if is_prime(elemento):
            if max_primo is None or elemento > max_primo:
                max_primo = elemento
    if max_primo is None:
        menor_elemento = min(coluna)
        for i in range(12):
            matriz[i][j] += menor_elemento
    else:
        for i in range(12):
            matriz[i][j] += max_primo

print("\nMatriz modificada:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()
