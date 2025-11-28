#ATM simulator

money = 0
while True:
    pin = (input('Enter your pin: '))
    if len(pin) != 4 or not pin.isdigit():
     print('Your pin must contain only 4 NUMBERS!!!')
     print('Enter your pin again')
    else:
        print('Pin poprwany.')
        break
while True:
    print('Press:')
    print('1 if you want to deposit money')
    print('2 if you want to withdraw money')
    print('3 if you want to check balance')
    print('4 if you want to check pin')
    print('5 if you want to change pin')
    print('6 if you want to quit')


    option = (input('Select the number: '))
    if option == '1':
        additional = int(input('How much do you want to deposit? '))
        money += additional
        print(f'Your deposit of {additional} money succed')
        decision = input(f'Do you want to deposit more money? y/n: ').upper()
        if decision == 'Y':
            additional_1 = int(input('Select amount you want to deposit: '))
            money += additional_1
            print(f'You deposited {additional_1} money')
    elif option == '2':  
           print('How much money do you want to withdraw?')
           amount = int(input(''))
           if amount > money:
              print('Not enough balance')
           else:
               money -= amount
               print(f'You withdraw {amount} money')
    elif option == '3':
        print(f'Your account balance is: {money}')
    elif option == '4':
        print(f'Your pin is: {pin}')
    elif option == '5':
        while True:
            new_pin = input(f'Select your new pin: ')
            if len(new_pin) == 4 and new_pin.isdigit():
               pin = new_pin
               print('Pin accepted')
               break
            else:
                print('Your pin must contain only 4 NUMBERS!!!')
                print('Enter your pin again')
    elif option == '6':
        print('Thanks for using ATM')
        break