###
# A program that checks if the name is women's
#
name = input('Enter the name: ')
formatted_name = name.capitalize()
if name[-1].lower() == 'a':
    print(f'{formatted_name} is a Polish female name')
else:
    print(f'{formatted_name} probably is not a Polish female name')
