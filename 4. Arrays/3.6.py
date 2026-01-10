# Mean using while
arr = [15,8,31,47,2,19]
i = total = 0
while i < len(arr):
    total += arr[i]
    i += 1
print("Array:", *arr)
print("Mean:", total/len(arr))
