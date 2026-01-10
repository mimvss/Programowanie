# Min and max with position
arr=[[-38,19],[5,40],[-7,11],[29,16]]
min_val=max_val=arr[0][0]
pos_min=pos_max=(0,0)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]<min_val:
            min_val=arr[i][j];pos_min=(i,j)
        if arr[i][j]>max_val:
            max_val=arr[i][j];pos_max=(i,j)
print(min_val,pos_min)
print(max_val,pos_max)
