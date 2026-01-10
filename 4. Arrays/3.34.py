# Identity matrix
def identity_matrix(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
for n in [3,5,8]:
    m=identity_matrix(n)
    for r in m:
        print(*r)
    print()
