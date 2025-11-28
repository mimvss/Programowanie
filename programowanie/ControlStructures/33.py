###
# A program that calculates dog's age
#
dog_age = int(input('Enter dog age in human years: '))
if dog_age < 3:
    dog_age = 10.5 * dog_age 
    print(f'Your dog is {dog_age} years old in dogs years.')
else:
    dog_age = 10.5 * 2 + 4 * (dog_age - 2)
    print(f'Your dog is {dog_age} years old in dogs years.')
