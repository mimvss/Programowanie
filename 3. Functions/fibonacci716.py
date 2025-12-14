# --- Plik: fibonacci.py ---

def f(n):
    # Pierwszy wyraz to 0
    if n == 1:
        return 0
    # Drugi wyraz to 1
    if n == 2:
        return 1
    
    # Jeśli n > 2, musimy policzyć sumę poprzednich
    a = 0  # To jest wyraz pierwszy
    b = 1  # To jest wyraz drugi
    
    # Pętla liczy od 3. wyrazu aż do n-tego
    for i in range(3, n + 1):
        wynik = a + b  # Suma dwóch poprzednich
        a = b          # Przesuwamy się: 'a' staje się starym 'b'
        b = wynik      # 'b' staje się nowym wynikiem
        
    return b