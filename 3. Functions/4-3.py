###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a, b, c):
    s = 0.5 * (a + b + c) #tu liczymy połowe obwodu trójkąta
    return math.sqrt(s * (s - a) * (s - b) * (s - c)) #na podstawie zmiennej s liczymy obszar trójkąta

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

print(f"The area of a triangle with sides {a}, {b}, {c} is {triangle_area(a, b, c):.0f}")