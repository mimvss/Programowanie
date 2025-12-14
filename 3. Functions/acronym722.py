def f(name):
    # Dzielimy zdanie na listę słów (rozdziela tam, gdzie są spacje)
    # np. "Internet of Things" zamieni się na ["Internet", "of", "Things"]
    slowa = name.split()
    
    wynik = ""
    
    # Przechodzimy przez każde słowo z listy
    for slowo in slowa:
        # Bierzemy pierwszą literę słowa (indeks 0) i doklejamy do wyniku
        wynik = wynik + slowo[0]
        
    return wynik