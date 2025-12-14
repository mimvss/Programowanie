# --- Plik: main.py ---
import numbers710  # Importujemy nasz plik numbers.py

# Test 1: Zakres <-7, 8>
# Ujemne parzyste tutaj to: -6, -4, -2 (czyli 3 liczby)
print(f"f(-7, 8) returns {numbers710.f(-7, 8)}")

# Test 2: Zakres <-1, 11>
# Ujemne liczby to tylko -1, ale ona nie jest parzysta (czyli 0 liczb)
print(f"f(-1, 11) returns {numbers710.f(-1, 11)}")