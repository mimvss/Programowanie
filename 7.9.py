# A program that check if the number on dice roll is special

import random
roll = random.randint(1,6)
check = roll == 1 or roll == 6
print(f' your roll is: {roll}')
print(f' Special number (1 or 6): {check}')