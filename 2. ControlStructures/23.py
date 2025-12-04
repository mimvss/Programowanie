# Timer that counts down to zero
# Last five seconds are printed in words

import time

number_words = {5: 'five', 4: 'four', 3: 'three', 2: 'two', 1: 'one'}

# Pobranie liczby sekund od użytkownika
seconds = int(input("Enter the number of seconds to count down: "))

for i in range(seconds, 0, -1):
    if i in number_words:
        print(number_words[i])
    else:
        print(i)
    time.sleep(1)  # czekaj 1 sekundę

print("Time's up!")
