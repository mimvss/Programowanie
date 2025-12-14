# --- Plik: main.py ---
import month73  # Importujemy nasz plik months.py

# 1. Pobieramy numer miesiąca od użytkownika
n = int(input("Enter month number: "))

# 2. Używamy funkcji z naszego modułu, żeby zdobyć nazwę
name = month73.month(n)

# 3. Wyświetlamy wynik
print("The name of month", n, "is", name)