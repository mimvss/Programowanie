# --- Plik: main.py ---
import digits79  # Importujemy nasz plik digits.py

# Test 1: Suma parzystych w 3124 (2 + 4 = 6)
print(f"f(3124, True) returns {digits79.f(3124, True)}")

# Test 2: Suma nieparzystych w 3124 (3 + 1 = 4)
print(f"f(3124, False) returns {digits79.f(3124, False)}")

# Test 3: Suma nieparzystych w 20576 (5 + 7 = 12)
print(f"f(20576, False) returns {digits79.f(20576, False)}")

# Test 4: Suma parzystych w 20576 (2 + 0 + 6 = 8)
print(f"f(20576, True) returns {digits79.f(20576, True)}")

# Test 5: Suma parzystych w 13115 (brak parzystych = 0)
print(f"f(13115, True) returns {digits79.f(13115, True)}")