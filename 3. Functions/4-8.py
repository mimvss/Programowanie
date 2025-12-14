#. Jej zadaniem jest przeliczenie godziny z formatu 24h na 12h.
def convert_to_12h(hours):
    smth = "am" # Domyślnie zakładamy, że jest rano (ante meridiem)
    if hours >= 12 and hours <= 23: 
        if hours != 12: # Jeśli jest 13, 14, 15.../ dla dwunastki nie odejmujemy nic, ale zmieniamy "am" na "pm".
            hours -= 12 # Odejmij 12 (np. 13 - 12 = 1)
        smth = "pm" # Zmień końcówkę na PM
    elif hours == 0:
        hours = 12
    return hours, smth

def time_string(hours, minutes, _format):
    if _format == '24':
        print(f"{hours:02d}:{minutes:02d}") #Dzięki temu zamiast 8:5 zobaczymy ładne 08:05
    else:
        hours, suffix = convert_to_12h(hours) #Jeśli format jest inny niż '24' (czyli '12'), najpierw wołamy funkcję convert_to_12h
        print(f"{hours:02d}:{minutes:02d}{suffix}")


time_string(15, 38, '24')
time_string(8, 3, '24')
time_string(0, 5, '24')
time_string(11, 15, '12')
time_string(0, 7, '12')
time_string(7, 30, '12')
time_string(12, 46, '12')
time_string(13, 10, '12')
time_string(19, 2, '12')
