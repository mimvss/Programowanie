# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
import math
a = input('a=')
a_side = int(a)
b = input('b=')
b_side = int(b)
c = input('c=')
c_side = int(c)
volume = a_side * b_side * c_side
surface = 2*(a_side * b_side + a_side * c_side + b_side * c_side)
print(f'The volume of the cuboid a= {a_side}, b= {b_side}, c= {c_side}, is {volume}.')
print(f'And the surface of that cuboid is {surface}')
