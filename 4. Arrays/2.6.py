# 2.5 - Main diagonal of matrix
matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(matrix)):
    matrix[i][i] = 1

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
