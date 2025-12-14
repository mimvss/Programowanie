# --- Plik: main.py ---

# Importujemy nasz własny moduł (plik keyboard.py)
def input_string(message):
    # Pobiera tekst od użytkownika
    wynik = input(message)
    return wynik

def input_integer(message):
    # Pobiera tekst i zamienia go na liczbę całkowitą (int)
    wynik = int(input(message))
    return wynik

def input_real(message):
    # Pobiera tekst i zamienia go na liczbę rzeczywistą/ułamkową (float)
    wynik = float(input(message))
    return wynik

def input_boolean(message):
    # Pobiera tekst, sprawdza czy to 'y' (tak). Zwraca Prawdę lub Fałsz.
    tekst = input(message)
    if tekst == 'y':
        return True
    else:
        return False

# 1. Wczytujemy dane używając funkcji z naszego modułu
first_name = input_string('Podaj imię: ')
last_name = input_string('Podaj nazwisko: ')
age = input_integer('Podaj wiek: ')
salary = input_real('Podaj wynagrodzenie: ')
is_salary_hidden = input_boolean('Ukryć pensję? (y/n): ')

# 2. Wyświetlamy raport
print('\nDATA RECORD')
print('=============')
print('Imię i nazwisko:', first_name, last_name)
print('Wiek:', age)

# 3. Decyzja czy pokazać pensję
# Jeśli użytkownik NIE chciał ukryć (czyli is_salary_hidden jest False), to drukujemy
if is_salary_hidden == False:
    print('Pensja:', salary)