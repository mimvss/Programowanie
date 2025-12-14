def power(x, n):
    # 1. Baza rekurencji (warunek stopu)
    # Każda liczba podniesiona do potęgi 0 daje 1.
    # To jest moment, w którym przestajemy wywoływać funkcję.
    if n == 0:
        return 1
    
    # 2. Krok rekurencyjny
    # Zgodnie ze wskazówką: x^n = x * x^(n-1)
    # Funkcja woła samą siebie dla potęgi o 1 mniejszej.
    return x * power(x, n - 1)

# --- Część główna programu ---

# Obliczamy 5 do potęgi 3
x = 5
n = 3
wynik = power(x, n)

# Wyświetlamy wynik
print(f"{x} do potęgi {n} wynosi: {wynik}")