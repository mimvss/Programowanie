# Ile liczb pierwszych chcemy
N = int(input("Enter the number of prime numbers: "))

count = 0  # licznik znalezionych liczb pierwszych
num = 2    # pierwsza liczba do sprawdzenia

print("Prime numbers:", end=' ')

while count < N:
    is_prime = True
    for i in range(2, num):  # sprawdzamy wszystkie liczby od 2 do num-1
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
        count += 1
    num += 1
