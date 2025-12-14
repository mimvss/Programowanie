# --- Plik: sequence.py ---

def f(n):
    # Zmienna na wynik (na początku pusty tekst)
    wynik = ""
    
    # Pętla od 1 do n (włącznie, dlatego n + 1)
    for i in range(1, n + 1):
        # Zamieniamy liczbę na tekst (str) i doklejamy do wyniku
        wynik = wynik + str(i)
        
    return wynik