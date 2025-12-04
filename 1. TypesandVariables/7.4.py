###
# A program that checks whether the tree may be cut down

import math

tree = int(input('Enter circumference of the tree in cm '))

diameter = tree / math.pi
diameter_valid = diameter >= 50
print(f'tree is ready to be cut down: {diameter_valid}')
