# 1. Funkcja: Centymetry -> Cale
def cm_to_inches(cm):
    return cm / 2.54

# 2. Funkcja: Stopy i Cale -> Centymetry
def feet_and_inches_to_cm(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 2.54

# --- CZĘŚĆ GŁÓWNA (To co widzisz na ekranie) ---
print("Co chcesz przeliczyć?")
print("1 - Centymetry na Cale")
print("2 - Stopy i Cale na Centymetry")

wybor = input("Wybierz 1 lub 2: ")

if wybor == '1':
   
    cm_input = float(input("Podaj długość w cm: "))
    wynik = cm_to_inches(cm_input)
    print(f"{cm_input} cm to {wynik:.2f} cali")

elif wybor == '2':
    feet_input = int(input("Podaj liczbę stóp: "))
    inches_input = float(input("Podaj liczbę cali: "))
    wynik = feet_and_inches_to_cm(feet_input, inches_input)
    print(f"{feet_input} stóp i {inches_input} cali to {wynik:.2f} cm")

else:
    print("Nie ma takiej opcji!")