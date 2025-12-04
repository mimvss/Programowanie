###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))
#month1 = month in range [0:12]
#if month1 > 12:
#    print('this month does not exist')
if month >= 1 and month <= 3 :
    quarter = +1
    print(f'Month {month} is in quarter {quarter}')
elif month > 3 and month <= 6:
    quarter = +2
    print(f'Month {month} is in quarter {quarter}')
elif month > 6 and month <= 9:
    quarter = +3
    print(f'Month {month} is in quarter {quarter}')
elif month > 0 and month <= 12:
    quarter = +4
    print(f'Month {month} is in quarter {quarter}')
else:
    print('This month does not exist')

