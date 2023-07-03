A = [[0] * 12 for _ in range(12)]
B = [[0] * 12 for _ in range(12)]

for i in range(12):
    for j in range(12):
        A[i][j] = i + j
        B[i][j] = i - j

C = [[0] * 12 for _ in range(12)]
for i in range(12):
    for j in range(12):
        for k in range(12):
            C[i][j] += A[i][k] * B[k][j]

for i in range(12):
    for j in range(12):
        print(C[i][j], end=" ")
    print()