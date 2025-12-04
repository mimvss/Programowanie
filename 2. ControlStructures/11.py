###
# Checking login and password
#
login = 'Stasiu'
password = 'abcd'
entered_login = input('Login: ')
entered_password = input('Password: ')
if login == entered_login and password == entered_password :
    print('You are logged in')
elif login == entered_login or password == entered_password:
     print('Incorrect login or password!!')
else :
     print('Both password and login are incorrect')