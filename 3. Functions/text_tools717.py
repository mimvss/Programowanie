# --- Plik: text_tools.py ---

def f(palindrome):
    # Tworzymy odwróconą wersję tekstu
    # [::-1] oznacza: idź od początku do końca, ale krokami -1 (czyli wstecz)
    odwrocony = palindrome[::-1]
    
    # Porównujemy oryginał z wersją odwróconą
    if palindrome == odwrocony:
        return True
    else:
        return False
