###
# Calculates the sum of the digits in a number
#
def sum_digits(number): #Definiujemy nową funkcję o nazwie sum_digits, która przyjmuje jeden argument (zmienną wejściową) o nazwie number
    s = 0 #pojemnik który będzie przechowywał sumę

    for ch in str(abs(number)): #oblicza wartość bezwzględną liczby, #abs zmienia np. -234 na 234
        digit = int(ch) #zamieniamy pojedyńczy znak na liczbę całkowitą
        s += digit #dodajemy cyfrę do naszej sumy

    return s #zwraca gotowy wynik

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number) #wyłowujemy naszą funkcję
print(f'The sum of the digits in the number {any_number} is {result}')

#pętla działanie:
#Bierzemy znak "4" jest w str po to by pętla for mogła zadziałać
#Zamieniamy go na liczbę 4 
#Dodajemy do sumy (0 + 4 = 4).