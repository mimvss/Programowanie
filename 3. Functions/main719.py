#--- Plik: main.py ---
import repeated719  # Importujemy nasz plik repeated.py

# Test 1: Brak powtórzeń (każda cyfra jest raz) -> Suma 0
print(f"f(1027) returns {repeated719.f(1027)}")

# Test 2: Cyfra 3 powtarza się trzy razy (3+3+3=9)
print(f"f(230335) returns {repeated719.f(230335)}")

# Test 3: Powtarzają się 5, 3 i 0. Sumujemy wszystkie ich wystąpienia.
print(f"f(513553007) returns {repeated719.f(513553007)}")