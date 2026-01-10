# Transpose
def transpose(m):
    return list(map(list,zip(*m)))

m=[[1,2,3],[4,5,6],[7,8,9]]
for r in transpose(m):
    print(*r)
