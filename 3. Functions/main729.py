# --- Plik: main.py ---

def factorial(n):
    # 1. Baza rekurencji (warunek stopu)
    # Silnia z 0 i 1 to zawsze 1. Tutaj funkcja przestaje wywoływać samą siebie.
    if n == 0 or n == 1:
        return 1
    
    # 2. Krok rekurencyjny
    # Silnia z n to: n * silnia z (n-1)
    if n > 1:
        return n * factorial(n - 1)

# --- Część główna programu ---

# Obliczamy silnię dla n = 5
n = 4
wynik = factorial(n)

# Wyświetlamy wynik
print(f"Silnia z {n} wynosi: {wynik}")