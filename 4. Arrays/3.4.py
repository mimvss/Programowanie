# Max and min without functions
arr = [-15,8,-31,47,-2,19]
min_val = max_val = arr[0]
for x in arr:
    if x < min_val: min_val = x
    if x > max_val: max_val = x
print("Min:", min_val)
print("Max:", max_val)
