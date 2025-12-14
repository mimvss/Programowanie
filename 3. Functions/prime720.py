def f(n):
    znalezione = 0  # Licznik: ile liczb pierwszych już znaleźliśmy
    liczba = 2      # Zaczynamy sprawdzanie od liczby 2 (pierwsza liczba pierwsza)
    
    # Pętla działa w nieskończoność, dopóki nie zwrócimy wyniku
    while True:
        # 1. Sprawdzamy, czy aktualna 'liczba' jest liczbą pierwszą
        jest_pierwsza = True
        
        # Dzielimy przez wszystko od 2 do liczby-1
        for i in range(2, liczba):
            if liczba % i == 0:
                jest_pierwsza = False # Jeśli się podzieliła, to nie jest pierwsza
                break
        
        # 2. Jeśli jest pierwsza, zwiększamy licznik
        if jest_pierwsza == True:
            znalezione += 1
            
            # Jeśli to jest ta n-ta, której szukamy, zwracamy ją
            if znalezione == n:
                return liczba
        
        # 3. Idziemy do kolejnej liczby (sprawdzamy 3, potem 4, potem 5 itd.)
        liczba += 1