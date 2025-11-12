#A program that calculates amount after the vat tax
#b is an amount after vat 

Amount = input('amount= ')
a = float(Amount)
v = 23 * a / 100
vat = round(v, 2)
b = a - v  
b1 = round(b, 2)
print(f'Vat = {vat} (23%), your amount after vat is {b1}')