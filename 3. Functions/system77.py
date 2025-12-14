# --- Plik: system.py ---

def f(binary_number):
    # Przechodzimy przez każdą cyfrę (znak) w tekście
    for znak in binary_number:
        # Jeśli znak NIE jest '0' I NIE jest '1', to to nie jest system binarny
        if znak != '0' and znak != '1':
            return False
            
    # Jeśli pętla się skończyła i nie znaleźliśmy błędu, to jest OK
    return True