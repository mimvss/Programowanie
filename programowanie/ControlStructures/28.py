###
# Program that simulates the operation of an electronic thermometer.
#
temperature = int(input("Choose temperature: "))
if temperature >= 35:
    print("It is extermely hot")
elif temperature >= 30 and temperature < 35:
    print("It is hot")
elif temperature >= 15 and temperature < 30:
    print('It is warm')
elif temperature >= 0 and temperature < 15:
    print('It is cold')
elif temperature < 0:
    print('Warning frost')