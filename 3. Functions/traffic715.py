def f(detector):
    osoby = 0
    
    # Przeglądamy każde zdarzenie (każdy plus lub minus)
    for znak in detector:
        if znak == "+":
            osoby += 1  # Ktoś wszedł
        elif znak == "-":
            osoby -= 1  # Ktoś wyszedł
            
        # Po każdej zmianie sprawdzamy, czy jest tłok (3 osoby lub więcej)
        if osoby >= 3:
            return True
            
    # Jeśli pętla się skończyła i nigdy nie było 3 osób, zwracamy Fałsz
    return False