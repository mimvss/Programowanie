# --- Plik: divisibility.py ---

def f(x, y):
    suma = 0
    
    # Sprawdzamy liczby od x do y (włącznie)
    for i in range(x, y + 1):
        
        # Warunek 1: podzielna przez 2 (i % 2 == 0)
        # Warunek 2: podzielna przez 3 (i % 3 == 0)
        # Warunek 3: NIEpodzielna przez 4 (i % 4 != 0)
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            suma += i
            
    return suma