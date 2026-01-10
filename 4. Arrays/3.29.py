# Create 2D
def create_2d_arr(x,y):
    return [[0]*y for _ in range(x)]
arr=create_2d_arr(3,5)
for r in arr:
    print(*r)
