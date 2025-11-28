###
# Write a program that prints a message when the specified car speed, read from the keyboard, has been exceeded
#
car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140
if car_speed > speed_limit_max:
    print(f'Warning! You drive too fast!')
elif car_speed < speed_limit_min:
    print(f'Warning! You drive too slow!')
else:
    print("Correct speed")
    