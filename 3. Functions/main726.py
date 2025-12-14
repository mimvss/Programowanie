# --- Plik: main.py ---
import separator726  # Importujemy nasz plik separator.py

# Test 1: University -> U-n-i-v-e-r-s-i-t-y
print(f'f("University") returns "{separator726.f("University")}"')

# Test 2: UE -> U-E
print(f'f("UE") returns "{separator726.f("UE")}"')

# Test 3: x -> x (brak myślnika, bo to tylko jedna litera)
print(f'f("x") returns "{separator726.f("x")}"')

# Test 4: Pusty tekst -> Pusty tekst
print(f'f("") returns "{separator726.f("")}"')