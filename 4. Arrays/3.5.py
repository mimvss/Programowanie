# Mean using for
arr = [15,8,31,47,2,19]
total = 0
for x in arr:
    total += x
print("Array:", *arr)
print("Mean:", total/len(arr))
