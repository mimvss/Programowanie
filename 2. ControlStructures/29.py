###
# A program that calculates and prints correct fee for the parked car
#
time = int(input('For how many hours do you want to park? '))
if time > 0 and time < 3:
    fee = 5
    print(f'For {time} hours you have to pay {fee} PLN')
elif time >= 3 and time <= 6:
    fee = 15
    print(f'For {time} hours you have to pay {fee} PLN')
elif time > 6:
    fee = 20
    print(f'For {time} hours you have to pay {fee} PLN')