# Bubble sort
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arrays = [[3,2,1],[5,1,4],[9,7,8]]
for a in arrays:
    print(bubblesort(a[:]))
