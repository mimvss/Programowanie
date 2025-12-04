###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
import random
# COMPUTER TURN
while True:
    # COMPUTER TURN
    computer = random.randint(1, 6)

    # YOUR TURN
    you = int(input('Guess the number (1-6): '))

    if not 1 <= you <= 6:
        print("Your number must be between 1 and 6")
    else:
        if you == computer:
            print("You won, congrats!!!")
        else:
            print("You lost :c try next time")

        print(f'Your guess: {you}')
        print(f'Computer number is: {computer}')

    # Ask to play again
    again = input("Play again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break




