# MyArrays module logic
arr = [7,3,8,5,2]

def second_largest(a):
    a = sorted(a)
    return a[-2]

def diff(a):
    return max(a)-min(a)

def median(a):
    a = sorted(a)
    return a[len(a)//2]

print("Second largest:", second_largest(arr))
print("Median:", median(arr))
print("Min and max:", min(arr),max(arr))
print("As string:", "-".join(map(str,arr)))
