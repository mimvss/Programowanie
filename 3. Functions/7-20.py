# Define the function f(n) that returns the n-th prime number.
# A prime number is a natural number greater than 1, divisible by 1 and that number.
# Sample result:
# f(1) returns 2
# f(5) returns 11

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1): #sprawdza dzielniki po przez pierwiastek, ponieważ jesli liczba sie nie pierwiastkuje to nie ma dzielników
        if x % i == 0: #nie jest wtedy liczbą pierwszą
            return False
    return True

def f(n):
    count = 0
    number = 1
    while count < n: #działa tak długo dopóki nie napotkamy na n liczb pierwszych
        number += 1 #bierze kolejną liczbę do sprawdzenia
        if is_prime(number): #sprawdzamy czy jest pierwsza
            count += 1
    return number

print(f(1))
print(f(5))