###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
if len(password) >=8:
    print("password ok")
else:
    print("password too short")    
