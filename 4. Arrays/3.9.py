# Compare arrays
def compare(a,b):
    if len(a)!=len(b): return False
    for i in range(len(a)):
        if a[i]!=b[i]: return False
    return True

pairs = [
(["water","book","sky"],["water","book","sky"]),
([True,False],[True,False,True]),
([5,3,1],[5,3,1]),
([3,2,1],[3,2])
]

for a,b in pairs:
    print("Array1:", *a)
    print("Array2:", *b)
    print("Same:", compare(a,b))
    print()
