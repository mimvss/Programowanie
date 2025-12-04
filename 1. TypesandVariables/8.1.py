###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

import math
r = float(input("Type your r: "))
circumference = 2 * math.pi * r
area = math.pi * r ** 2
area1 = round(area, 2)
circumference1 = round(circumference, 2)

print(f'Your r: {r} --> circumference: {circumference1} --> area: {area1}')