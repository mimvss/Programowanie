# --- Plik: pword.py ---

def f(password):
    # 1. Warunek długości: jeśli jest krótsze niż 6, od razu odrzucamy
    if len(password) < 6:
        return False
    
    # 2. Warunek unikalności: sprawdzamy każdy znak po kolei
    for znak in password:
        # Jeśli jakikolwiek znak występuje w haśle więcej niż 1 raz -> Fałsz
        if password.count(znak) > 1:
            return False
            
    # Jeśli przeszliśmy pętlę i nie znaleźliśmy duplikatów -> Prawda
    return True