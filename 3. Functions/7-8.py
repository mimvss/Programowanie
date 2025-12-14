# The vending machine accepts 1, 2 and 5 PLN coins.
# Define a function f(amount_to_pay) that returns the minimum number of coins that can 
# be used to pay for the purchased product.
# Sample result:
# f(23) returns 6
# f(8) returns 3
# f(2) returns 1
# f(0) returns 0

def f(amount):
    coins = amount // 5 #oblicza ile mozna wydać 5 
    amount -= coins * 5 #oblicza wartość wydanych monet 5, aby pozostawić reszte
    coins += amount // 2 #oblicza ile monet 2 można wydać z pozostałej reszty i dodaje to do całkowitego licznika monet
    amount -= (amount // 2) * 2 #oblicza wartość wydanych monet
    coins += amount #dodaje pozostąła reszte
    return coins #zwraca ilość wydanych monet

print(f(23))
print(f(8))
print(f(2))
print(f(0))