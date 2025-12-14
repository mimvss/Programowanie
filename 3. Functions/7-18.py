# A sentence is an ordered group of words separated by spaces.
# Define a function f(sentence) that returns a sentence with spaces removed.
# Sample result:

# f("integrated development environment") returns
# "integrateddevelopmentenvironment"
# f("A programming language is a system of notation for writing computer programs") returns
# "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"

def f(sentence):
    res = ""
    for ch in sentence: #bierze każdy znak ch ze zdania jeden po drugim
        if ch != ' ': #sprawdza czy ch nie jest spacją
            res += ch #dopisauje nam do naszego magazynu litery które nie są spacją
    return res

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))