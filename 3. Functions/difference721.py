# --- Plik: difference.py ---

def f(number1, number2, number3):
    # Funkcja max() znajduje największą liczbę z podanych
    najwieksza = max(number1, number2, number3)
    
    # Funkcja min() znajduje najmniejszą liczbę z podanych
    najmniejsza = min(number1, number2, number3)
    
    # Obliczamy różnicę
    wynik = najwieksza - najmniejsza
    
    return wynik