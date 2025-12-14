def hide(card_number):
    # Karta ma 16 cyfr.
    # Bierzemy pierwsze 2 cyfry (od 0 do 2)
    poczatek = card_number[0:2]
    
    # Bierzemy ostatnie 4 cyfry (minus oznacza liczenie od końca)
    koniec = card_number[-4:]
    
    # Sklejamy: początek + 10 gwiazdek + koniec
    # (16 cyfr - 2 widoczne - 4 widoczne = 10 ukrytych)
    wynik = poczatek + "**********" + koniec
    
    return wynik