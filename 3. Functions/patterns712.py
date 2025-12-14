# --- Plik: patterns.py ---

def f(n):
    # Zmienna, w której budujemy wynik
    wynik = ""
    
    # Pętla wykonuje się n razy (tyle ile chcemy gwiazdek)
    for i in range(n):
        wynik = wynik + "*"
        
        # Jeśli to NIE jest ostatnia gwiazdka, dodajemy ukośnik
        # (n - 1 to indeks ostatniego elementu)
        if i < n - 1:
            wynik = wynik + "/"
            
    return wynik