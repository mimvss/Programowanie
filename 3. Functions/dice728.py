# --- Plik: dice.py ---

def f(dice):
    # Zmienne do śledzenia rekordu
    max_powtorzen = 0  # Najdłuższa seria jaką znaleźliśmy
    zwycieska_cyfra = ""  # Cyfra, która miała tę serię
    
    # Zmienne pomocnicze (tymczasowe)
    aktualna_cyfra = ""
    aktualny_licznik = 0
    
    # Przechodzimy przez każdą cyfrę w ciągu
    for cyfra in dice:
        # Jeśli ta cyfra jest taka sama jak poprzednia
        if cyfra == aktualna_cyfra:
            aktualny_licznik += 1
        else:
            # Jeśli to nowa cyfra, resetujemy licznik dla niej
            aktualna_cyfra = cyfra
            aktualny_licznik = 1
            
        # Sprawdzamy, czy obecna seria pobiła rekord
        if aktualny_licznik > max_powtorzen:
            max_powtorzen = aktualny_licznik
            zwycieska_cyfra = aktualna_cyfra
            
    # Funkcja ma zwrócić cyfrę jako liczbę (int)
    return int(zwycieska_cyfra)