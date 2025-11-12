#A program that calculates discount of the product
#c = price after discount
#r = reduction

Price = input('Product price= ')
a = float(Price)
Discout = input('Discount %= ')
b = float(Discout)
c = a - b * a / 100
c1 = round(c, 2)
r = a - c
r1 = round(r, 2)
print(f'Original price: {a}, discount %: {b}.')
print(f'Price after discount: {c1}, you are saving: {r1}')
