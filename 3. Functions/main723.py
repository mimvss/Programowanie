# --- Plik: main.py ---
import pword723  # Importujemy nasz plik pword.py

# Test 1: Za krótkie (False)
print(f'f("ax15") returns {pword723.f("ax15")}')

# Test 2: Ma duplikat ("o" występuje 2 razy) -> False
print(f'f("book123") returns {pword723.f("book123")}')

# Test 3: Długie i unikalne -> True
print(f'f("A2water3") returns {pword723.f("A2water3")}')

# Test 4: Długość 6 i unikalne -> True
print(f'f("qwerty") returns {pword723.f("qwerty")}')

# Test 5: Puste (za krótkie) -> False
print(f'f("") returns {pword723.f("")}')