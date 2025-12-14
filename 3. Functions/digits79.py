# --- Plik: digits.py ---

def f(number, even):
    suma = 0
    
    # Zamieniamy liczbę na napis, żeby móc pętlą brać każdą cyfrę
    for znak in str(number):
        cyfra = int(znak) # Zamieniamy znak z powrotem na liczbę
        
        # Sprawdzamy, czy cyfra jest parzysta (dzieli się przez 2 bez reszty)
        jest_parzysta = (cyfra % 2 == 0)
        
        # WARIANT A: Szukamy parzystych (even jest True) i cyfra jest parzysta
        if even == True and jest_parzysta == True:
            suma += cyfra
            
        # WARIANT B: Szukamy nieparzystych (even jest False) i cyfra jest nieparzysta
        if even == False and jest_parzysta == False:
            suma += cyfra
            
    return suma