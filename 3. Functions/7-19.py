# Define a function f(number) that returns the sum of repeated digits in a number.
# Sample result:
# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21

def f(number):
    _sum = 0
    digit_count = {} #sluzy do przechowywania ile razy widział daną liczbę
    for ch in str(number): #pętla przechodzi przez liczbę zmieniona na napis
        count = digit_count.get(ch, 0) #sprawdza ile razy widział liczbe (ch, 0) zabezpieczenie jesli cyfry nie ma w slowniku
        digit = int(ch) #zamieniamy spowrotem na liczbe
        if count == 1: #jeśli napotka liczbe poraz 2
            _sum += digit * 2 #dodajemy liczbe pomnozona razy dwa
        elif count > 1: 
            _sum += digit
        digit_count[ch] = count + 1
    return _sum

print(f(1027))
print(f(230335))
print(f(513553007))
