# --- Plik: coins.py ---

def f(amount_to_pay):
    liczba_monet = 0
    
    # 1. Sprawdzamy, ile razy mieści się 5 zł
    # Operator // to dzielenie bez reszty (np. 23 // 5 = 4)
    liczba_monet += amount_to_pay // 5 
    
    # Obliczamy resztę, która została do wydania (operator %)
    amount_to_pay = amount_to_pay % 5 
    
    # 2. Sprawdzamy, ile razy mieści się 2 zł w tym, co zostało
    liczba_monet += amount_to_pay // 2
    amount_to_pay = amount_to_pay % 2
    
    # 3. To co zostało, to monety 1 zł
    liczba_monet += amount_to_pay
    
    return liczba_monet

print(f"f(23) returns {f(23)}")
print(f"f(8) returns {f(8)}")
print(f"f(2) returns {f(2)}")
print(f"f(0) returns {f(0)}")



