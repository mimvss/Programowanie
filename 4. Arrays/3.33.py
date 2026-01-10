# Swap columns
arr=[[1,2,3,4,5],[6,7,8,9,0],[9,8,7,6,5]]
for r in arr:
    r[0],r[-1]=r[-1],r[0]
for r in arr:
    print(*r)
