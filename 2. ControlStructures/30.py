###
# A program that checks user age and checks what group age they belong to
#
age = int(input('Choose your age: '))
if age > 0 and age < 13:
    group_age = 'Child'
    print(f'You belong to {group_age} group age')
elif age >= 13 and age <= 19:
    group_age = 'Teen'
    print(f'You belong to {group_age} group age')
elif age >= 20 and age <= 64:
    group_age = 'Adult'
    print(f'You belong to {group_age} group age')
else:
    group_age = 'Senior'
    print(f'You belong to {group_age} group age')
