# --- Plik: main.py ---

def sum_natural(n):
    # 1. Baza rekurencji (warunek stopu)
    # Jeśli n wynosi 1, to suma wynosi po prostu 1. Nie ma czego dodawać.
    if n == 1:
        return 1
    
    # 2. Krok rekurencyjny
    # Suma dla n to: n + suma dla (n-1)
    # Np. suma dla 5 to: 5 + suma liczb od 1 do 4
    return n + sum_natural(n - 1)

# --- Część główna programu ---

# Zadanie każe policzyć sumę dla zakresu <1, 10>, czyli n = 10
n = 10
wynik = sum_natural(n)

# Wyświetlamy wynik
print(f"Suma liczb naturalnych w zakresie <1,{n}> wynosi: {wynik}")