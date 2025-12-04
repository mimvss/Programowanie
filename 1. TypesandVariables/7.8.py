###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print(f'Your first roll is: {dice_roll_1}')
print(f'Your second roll is: {dice_roll_2}')
print(f'Your third roll is: {dice_roll_3}')
print(f'Total of your rolls is: {total}')