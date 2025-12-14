# A palindrome is an expression that sounds the same when read backwards.
# Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise.
# Sample result:
# f("radar") returns True
# f("12-11-21") returns True
# f("book") returns False

def f(palindrome):
    for i, ch in enumerate(palindrome): #pętla przechodzi przez każdy znak ch
        if ch != palindrome[-i-1]: #sprawdza czy obecny znak ch jest różny od odpowiadającemu mu znaku z drugiej strony
            return False
    return True

print(f("radar"))
print(f("12-11-21"))
print(f("book"))