def f(number):
    suma = 0
    tekst = str(number)  # Zamieniamy liczbę na napis, np. "230335"
    
    # Przechodzimy przez każdą cyfrę w tym napisie
    for cyfra in tekst:
        # Sprawdzamy, ile razy ta konkretna cyfra występuje w całym napisie
        if tekst.count(cyfra) > 1:
            # Jeśli więcej niż 1 raz, to dodajemy ją do sumy
            suma += int(cyfra)
            
    return suma

