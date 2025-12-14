# --- Plik: main.py ---
import divisibility725  # Importujemy nasz plik divisibility.py

# Test 1: Zakres 1-20
# Liczby podzielne przez 2 i 3 (czyli przez 6) to: 6, 12, 18.
# 12 odpada, bo dzieli się przez 4. Zostaje 6 i 18. Suma = 24.
print(f"f(1, 20) returns {divisibility725.f(1, 20)}")

# Test 2: Zakres 10-30
# Liczby podzielne przez 6 to: 12, 18, 24, 30.
# 12 i 24 odpadają (bo dzielą się przez 4). Zostaje 18 i 30. Suma = 48.
print(f"f(10, 30) returns {divisibility725.f(10, 30)}")