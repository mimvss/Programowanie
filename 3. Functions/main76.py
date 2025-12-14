# --- Plik: main.py ---
import maskin76  # Importujemy nasz plik masking.py

# 1. Numer karty z przykładu (jako napis/tekst)
numer_karty = "5290312400019022"

# 2. Używamy funkcji z modułu, żeby ukryć cyfry
ukryty_numer = maskin76.hide(numer_karty)

# 3. Wyświetlamy wynik
print("Oryginał:", numer_karty)
print("Po ukryciu:", ukryty_numer)