# Swap rows
arr=[[1,2,3,4,5],[6,7,8,9,0],[9,8,7,6,5]]
print("Before:",arr)
arr[0],arr[-1]=arr[-1],arr[0]
print("After:",arr)
