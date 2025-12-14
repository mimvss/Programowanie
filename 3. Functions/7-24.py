# An expression contains operators for adding and subtracting single-digit numbers.
# Define a function f(expression) that returns the value of the expression.
# Sample result:
# f("2+3") returns 5
# f("3+8+1") returns 12
# f("2+3-4+5-0") returns 6

def f(expression):
    total = 0
    op = 1

    for ch in expression:
        if ch == '+':
            op = 1 #liczba dodatnia jesli trafimy w princie na +
        elif ch == '-':
            op = -1 #liczba ujemna
        else:
            total += op * int(ch) #jesli trafimy na liczbe mnozymy ją przez op, czyli zmieniamy jej znak

    return total

print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))