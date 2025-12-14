# --- Plik: text_utils.py ---

def f(sentence):
    # Funkcja .replace("co", "na co") zamienia jeden tekst na inny.
    # Tutaj zamieniamy spację " " na pusty tekst "" (czyli ją usuwamy).
    wynik = sentence.replace(" ", "")
    
    return wynik