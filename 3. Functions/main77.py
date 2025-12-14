# --- Plik: main.py ---
import system77  # Importujemy nasz plik system.py

# Przykład 1: Poprawna liczba binarna
numer1 = "101101"
wynik1 = system77.f(numer1)
print(f"f('{numer1}') returns {wynik1}")

# Przykład 2: Błędna liczba (ma '3' i 'a')
numer2 = "1311a10100"
wynik2 = system77.f(numer2)
print(f"f('{numer2}') returns {wynik2}")