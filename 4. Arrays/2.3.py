# 2.2 - Monthly expenses statistics
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]

food = transport = utilities = 0
week_totals = []

for week in monthly_expenses:
    food += week[0]
    transport += week[1]
    utilities += week[2]
    week_totals.append(sum(week))

total = sum(week_totals)

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', transport)
print('Utilities:', utilities)
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', total)
