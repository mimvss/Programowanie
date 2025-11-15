###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius = int(input("Input temperature in celsius degrees: "))

#celsius to fahrenheit

farenheiht = celsius * 1.8 + 32

#celsius to kelvin

kelvin = celsius + 273.15

print(f'Degrees in celsius: {celsius} --> degrees in fahrenheit: {farenheiht} --> degrees in kelvin {kelvin}')