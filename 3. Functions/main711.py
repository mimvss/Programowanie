# --- Plik: main.py ---
import logic711  # Importujemy nasz plik logic.py

# Test 1: Mamy -4 (jest ujemna), więc powinno być True
print(f"f(11, 6, -4) returns {logic711.f(11, 6, -4)}")

# Test 2: Same dodatnie liczby, więc powinno być False
print(f"f(5, 4, 14) returns {logic711.f(5, 4, 14)}")