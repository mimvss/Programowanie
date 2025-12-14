# --- Plik: main.py ---
import traffic715  # Importujemy nasz plik traffic.py

# Test 1: Dochodzi do 3 osób (True)
print(f'f("+-+++-+---") returns {traffic715.f("+-+++-+---")}')

# Test 2: Ludzie wchodzą i wychodzą pojedynczo (False)
print(f'f("+-+-+-+-") returns {traffic715.f("+-+-+-+-")}')

# Test 3: Maksymalnie 2 osoby (False)
print(f'f("+-++-+--") returns {traffic715.f("+-++-+--")}')

# Test 4: W pewnym momencie wchodzi trzecia osoba (True)
print(f'f("+-++-++---") returns {traffic715.f("+-++-++---")}')