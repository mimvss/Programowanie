# Define the function f(n), which returns the n-th value of the Fibonacci sequence. 
# The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. 
# Each subsequent value is the sum of the previous two. Sample result:
# f(5) returns 3
# f(9) returns 21

def f(n):
    previous = 0 #pierwsza liczba ciągu
    current = 1 #druga liczba ciągu
    for _ in range(n-2): #do obliczenia n-tej liczby
        temp = previous + current #obliczamy nową sumę (z dwóch ostatnich)
        previous = current #stara obecna staje się poprzednią
        current = temp #nowa obliczona staje się obecną
 
    return current

print(f(5))
print(f(9))