# --- Plik: main.py ---
import myrange75  # Importujemy nasz plik my_range.py

# 1. Pobieramy liczbę od użytkownika
num = int(input("A number: "))

# 2. Ustalamy zakres tak jak na obrazku <2, 15>
start = 2
end = 15

# 3. Sprawdzamy, czy liczba jest w zakresie
# Funkcja zwróci True lub False
is_inside = myrange75.check_range(num, start, end)

# 4. Wyświetlamy wynik
# Jeśli is_inside to Prawda, piszemy 'yes', w przeciwnym razie 'no'
if is_inside:
    print(f"Number {num} in the range <{start},{end}>: yes")
else:
    print(f"Number {num} in the range <{start},{end}>: no")