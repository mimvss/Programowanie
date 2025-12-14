# Define the function f(n), which returns numbers from 1 to n as a string. Sample result:
# f(11) returns "1234567891011"
# f(4) returns "1234"

def f(n):
    text = ""
    for i in range(1,n+1): #pętla przechodzi przez wszystkie liczby od 1 do n.
        text += str(i) #w każdym obrocie pętli aktualna liczba i jest zmieniana na text
    return text

print(f(11))
print(f(4))