# --- Plik: math_expr.py ---

def f(expression):
    # 1. Na start bierzemy pierwszą cyfrę z tekstu i zamieniamy na liczbę
    wynik = int(expression[0])
    
    # 2. Pętla przechodzi przez resztę tekstu.
    # range(1, len, 2) oznacza: zacznij od znaku nr 1, idź do końca, skacz co 2.
    # Dzięki temu trafiamy zawsze na operatory (+ lub -).
    for i in range(1, len(expression), 2):
        operator = expression[i]        # To jest znak (+ lub -)
        kolejna_liczba = int(expression[i+1]) # To jest cyfra stojąca za znakiem
        
        # Wykonujemy działanie
        if operator == "+":
            wynik = wynik + kolejna_liczba
        elif operator == "-":
            wynik = wynik - kolejna_liczba
            
    return wynik