# --- Plik: months.py ---

def month(n):
    # Lista nazw miesięcy. 
    # Pierwszy element jest pusty "", żeby styczeń był pod indeksem 1, a nie 0.
    month_names = ["", "January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    
    # Zwracamy nazwę spod numeru n
    return month_names[n]