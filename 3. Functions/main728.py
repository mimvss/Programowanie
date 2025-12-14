# --- Plik: main.py ---
import dice728  # Importujemy nasz plik dice.py

# Test 1: "5233165554211"
# Piątka (5) występuje 3 razy pod rząd. To najdłuższa seria. Wynik: 5.
print(f'f("5233165554211") returns {dice728.f("5233165554211")}')

# Test 2: "2133"
# Trójka (3) występuje 2 razy pod rząd. Wynik: 3.
print(f'f("2133") returns {dice728.f("2133")}')