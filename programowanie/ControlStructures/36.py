###
#program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard
#
Products = int(input('Enter number of products: '))
product_price = int(input('Enter product price: '))
if Products >= 3:
    # total = product_price * 2 + (Products - 2) * (product_price - product_price * 25 / 100)
    total = product_price * 2 + (Products - 2) * product_price * 0.75
    print(f'Amount to pay: {total}')
else:
    total = product_price * Products
    print(f'Amount to pay: {total}')