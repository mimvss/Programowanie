###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ').lower()
while program != 'j' and program != 'u' and program != 's':
    print('You entered incorrect program!')
    program = input('Select correct program: ').lower()

extra_rinse = input('Extra rinse? (y/n): ').lower()
extra_spin = input('Extra spin? (y/n): ').lower()
if program == 'j':
    total_washing_time += 40
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20
if extra_rinse == 'y':
    extra_rinse = True
    total_washing_time += 15
else:
    extra_rinse = False
if extra_spin == 'y':
    extra_spin = True
    total_washing_time += 9
else:
    extra_spin = False
print(f'Selected program {program}.')
print(f'Extra spin {extra_spin}')
print(f'Extra rinse {extra_rinse}')
print(f'Total washing time {total_washing_time}')

