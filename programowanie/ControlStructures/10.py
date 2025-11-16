#Write a program that checks what number was entered from the keyboard and prints one of the messages below. Then run the program and check the following numbers:

liczba = int(input('podaj liczbe: '))

if liczba < 0: 
    print('negative')
elif liczba == 0:
    print("0")
else:
    print("positive")