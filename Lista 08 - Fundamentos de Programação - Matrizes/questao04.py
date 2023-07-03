import random

linhas = 14
colunas = 32

matriz = [[random.randint(1, 100) for _ in range(colunas)] for _ in range(linhas)]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()

maior_valor = matriz[0][0]
linha_maior_valor = 0
coluna_maior_valor = 0

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha_maior_valor = i
            coluna_maior_valor = j

print(f"O maior valor está na linha {linha_maior_valor + 1} e coluna {coluna_maior_valor + 1}.")