# --- Plik: main.py ---
import litera74  # Importujemy nasz plik letters.py

# 1. Definiujemy tekst z zadania
text = "You never get a second chance to make a first impression"

# 2. Używamy funkcji z modułu, żeby policzyć literę 'e'
# Przekazujemy tekst i literkę, której szukamy
number = litera74.count_letter(text, 'e')

# 3. Wyświetlamy wynik dokładnie jak na obrazku
print(text)
print("The number of letter 'e':", number)