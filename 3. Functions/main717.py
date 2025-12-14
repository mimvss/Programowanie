# --- Plik: main.py ---
import text_tools717  # Importujemy nasz plik text_tools.py

# Test 1: radar (od tyłu to też radar) -> True
print(f'f("radar") returns {text_tools717.f("radar")}')

# Test 2: 12-11-21 (od tyłu to 12-11-21) -> True
print(f'f("12-11-21") returns {text_tools717.f("12-11-21")}')

# Test 3: book (od tyłu to koob) -> False
print(f'f("book") returns {text_tools717.f("book")}')