###
# A program that checks if the item is worth purchasing
#
current_price = int(input('Enter current price: '))
previous_price = int(input('Enter previous price: '))
if current_price < previous_price:
    discount = previous_price - current_price
    discount_percent = (discount / previous_price) * 100
    discount_percent = round(discount_percent)
    print(f'Buy the product!')
    print(f'Product price reduced by {discount_percent}%')

