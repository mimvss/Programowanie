###
# A program that checks EAN-13 number
#
ean13 = (input('Enter EAN-13 number: '))
while len(ean13) != 13 or not ean13.isdigit():
    print('Incorrect EAN-13 number')
    ean13 = (input('Enter number again:'))
else:
    print('Article number is correct')

if ean13[ :3] == '590':
    print('Article manufactured in Poland')

    
