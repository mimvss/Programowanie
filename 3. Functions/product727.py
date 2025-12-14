# --- Plik: product.py ---

def f(product_code):
    # product_code to tekst (np. "1082")
    
    # 1. Pobieramy trzy pierwsze cyfry i zamieniamy je na liczby
    pierwsza = int(product_code[0])
    druga    = int(product_code[1])
    trzecia  = int(product_code[2])
    
    # 2. Pobieramy czwartą cyfrę (kontrolną)
    czwarta_kontrolna = int(product_code[3])
    
    # 3. Obliczamy sumę pierwszych trzech
    suma = pierwsza + druga + trzecia
    
    # 4. Obliczamy resztę z dzielenia sumy przez 7
    reszta = suma % 7
    
    # 5. Sprawdzamy: czy obliczona reszta jest taka sama jak czwarta cyfra?
    if reszta == czwarta_kontrolna:
        return True
    else:
        return False