# --- Plik: numbers.py ---

def f(x, y):
    licznik = 0
    
    # Pętla sprawdza liczby od x do y (włącznie, dlatego y + 1)
    for liczba in range(x, y + 1):
        
        # Warunek 1: Liczba musi być ujemna (< 0)
        # Warunek 2: Liczba musi być parzysta (dzielić się przez 2 bez reszty)
        if liczba < 0 and liczba % 2 == 0:
            licznik += 1
            
    return licznik