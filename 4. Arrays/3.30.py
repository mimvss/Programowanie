# Multiplication table
arr=[[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        arr[i][j]=(i+1)*(j+1)
for r in arr:
    print(*r)
