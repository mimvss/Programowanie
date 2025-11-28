# Read decimal number
decimal = int(input("Enter decimal number: "))
original = decimal

binary = ""  # tu będziemy budować wynik

if decimal == 0:
    binary = "0"
else:
    while decimal > 0:
        remainder = decimal % 2          # reszta z dzielenia przez 2
        binary = str(remainder) + binary # doklejamy z przodu
        decimal = decimal // 2           # dzielenie całkowite

print(f"{original}(10) = {binary}(2)")

